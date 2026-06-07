class Usuario():
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        
    def verificar_senha(self, senha_digitada):
        return self.senha == senha_digitada
    
class Produto:
    def __init__(self, nome, qtd, preco):
        self.nome = nome
        self.qtd = qtd
        self.preco = preco
        
    def adicionar_novo(self, quantidade_nova):
        self.qtd += quantidade_nova
           
    def remover_unidade(self, quantidade_a_remover):
        if quantidade_a_remover <= self.qtd:
            self.qtd -= quantidade_a_remover
        
        else:
            print("Erro: Estoque insuficiente!")
        
    def editar_nome(self, novo_nome):
        self.nome = novo_nome    
    
    def editar_preço(self, novo_preço):
        self.preco = novo_preço  
    
    def visualizar_produto(self):
        return f"{self.nome} - Quantidade: {self.qtd} - Preço: R${self.preco:.2f}"
        
class Cliente:
    def __init__(self, id_cliente, nome):
        self.id = id_cliente
        self.nome = nome
        
    def visualizar_cliente(self):
        return f"[{self.id}] {self.nome}"
    
              
class Sistema:
    
    def __init__(self):
        self.clientes = []
        self.estoque = []
        self.vendas = []
        self.valor_caixa = 0.0
        self.usuarios = []  # Lista para armazenar usuários do sistema
    
    
    def exibir_clientes(self):
        return [cliente.visualizar_cliente() for cliente in self.clientes]
    
    def buscar_cliente(self, id_cliente):
     for cliente in self.clientes:
        if str(cliente.id) == str(id_cliente): # str() evita erro se um for int e outro string
            return cliente
     return None

    def exibir_estoque(self):
        return [produto.visualizar_produto() for produto in self.estoque]
    
    def cadastrar_cliente(self, novo_cliente):
        self.clientes.append(novo_cliente)
        
    def cadastrar_produto(self, novo_produto):
        self.estoque.append(novo_produto)
        
    def buscar_produto(self, nome_produto):
     for produto in self.estoque:
        if produto.nome.strip().title() == nome_produto.strip().title():
            return produto
     return None
        
    def adicionar_novo(self, produto, quantidade):
        for item in self.estoque:
            if item.nome == produto.nome:
                item.adicionar_novo(quantidade)
                break
        else:
            print("Produto não encontrado no estoque.")
    
    def remover_cliente(self, id_cliente):
        self.clientes = [cliente for cliente in self.clientes if cliente.id != id_cliente]
       
    def remover_produto(self, nome_produto):
        self.estoque = [produto for produto in self.estoque if produto.nome != nome_produto]  
        
    def buscar_usuario(self, login):
        
      for u in self.usuarios:
        if u.login == login:
            return u
      return None
  
    def autenticar(self, login_digitado, senha_digitada):
        usuario = self.buscar_usuario(login_digitado)
        
        if usuario and usuario.verificar_senha(senha_digitada):
            return usuario  # Login com sucesso
            
        return None 
     
    def remover_usuario(self, login):
       self.usuarios = [u for u in self.usuarios if u.login != login]
      
        
class Produto_Perecivel(Produto):
    def __init__(self, nome, qtd, preco, data_validade):
        super().__init__(nome, qtd, preco)
        self.data_validade = data_validade
        
    def visualizar_produto(self):
        return f"{self.nome} - Quantidade: {self.qtd} - Preço: R${self.preco:.2f} - Validade: {self.data_validade}"
    
    def verificar_validade(self, data_atual):
        if data_atual > self.data_validade:
            return f"Produto {self.nome} está vencido!"
        else:
            return f"Produto {self.nome} está dentro da validade."         
        

class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.preco * quantidade
        
    
    def processar_venda(self, sistema):
     if self.produto.qtd >= self.quantidade:
        self.produto.remover_unidade(self.quantidade)
        sistema.valor_caixa += self.valor_total
        # Retorna uma TUPLA com dois valores: (True, "mensagem")
        return True, f"Venda processada: {self.cliente.nome} comprou {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"
     else:
        # Retorna uma TUPLA com dois valores: (False, "mensagem")
        return False, "Erro: Estoque insuficiente para processar a venda."
    
    def visualizar_venda(self):
        return f"Venda: {self.cliente.nome} comprou {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"
    
    def cancelar_venda(self, sistema):
        self.produto.adicionar_novo(self.quantidade)
        sistema.valor_caixa -= self.valor_total
        return f"Venda cancelada: {self.cliente.nome} cancelou a compra de {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"