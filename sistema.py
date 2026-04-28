


class Produto:
    def __init__(self, nome, qtd, preço):
        self.nome = nome
        self.qtd = qtd
        self.preço = preço
        
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
        self.preço = novo_preço  
    
    def visualizar_produto(self):
        return f"{self.nome} - Quantidade: {self.qtd} - Preço: R${self.preço:.2f}"
        
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
        self.valor_caixa = 0.0
    
    
    def exibir_clientes(self):
        return [cliente.visualizar_cliente() for cliente in self.clientes]
    
    def exibir_estoque(self):
        return [produto.visualizar_produto() for produto in self.estoque]
    
    def cadastrar_cliente(self, novo_cliente):
        self.clientes.append(novo_cliente)
        
    def cadastrar_produto(self, novo_produto):
        self.estoque.append(novo_produto)
        
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
        
class Produto_Perecivel(Produto):
    def __init__(self, nome, qtd, preço, data_validade):
        super().__init__(nome, qtd, preço)
        self.data_validade = data_validade
        
    def visualizar_produto(self):
        return f"{self.nome} - Quantidade: {self.qtd} - Preço: R${self.preço:.2f} - Validade: {self.data_validade}"
    
    def verificar_validade(self, data_atual):
        if data_atual > self.data_validade:
            return f"Produto {self.nome} está vencido!"
        else:
            return f"Produto {self.nome} está dentro da validade."         
        

class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto9
        self.quantidade = quantidade
        self.valor_total = produto.preço * quantidade
        
    def processar_venda(self, sistema):
        if self.produto.qtd >= self.quantidade:
            self.produto.remover_unidade(self.quantidade)
            sistema.valor_caixa += self.valor_total
            return f"Venda processada: {self.cliente.nome} comprou {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"
        else:
            return "Erro: Estoque insuficiente para processar a venda."
        
    def visualizar_venda(self):
        return f"Venda: {self.cliente.nome} comprou {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"
    
    def cancelar_venda(self, sistema):
        self.produto.adicionar_novo(self.quantidade)
        sistema.valor_caixa -= self.valor_total
        return f"Venda cancelada: {self.cliente.nome} cancelou a compra de {self.quantidade} de {self.produto.nome} por R${self.valor_total:.2f}"

p1 = Cliente(1010, "Joao")
p2 = Cliente(1020, "Maria")
p3 = Cliente(1030, "Pedro")
sistema = Sistema()
sistema.cadastrar_cliente(p1)
sistema.cadastrar_cliente(p2)
sistema.cadastrar_cliente(p3)
prod1 = Produto("Coca-cola", 10, 5.0)
prod2 = Produto("Pepsi", 15, 4.5)
sistema.cadastrar_produto(prod1)
sistema.cadastrar_produto(prod2) 
print(prod1.visualizar_produto())
print(prod2.visualizar_produto())
sistema.adicionar_novo(prod1, 5) 
print(prod1.visualizar_produto())
p4 = Cliente(1040, "Ana")
sistema.cadastrar_cliente(p4)
print(sistema.exibir_clientes())
print(sistema.exibir_estoque())
prod4 = Produto("Fanta", 20, 4.0)
sistema.cadastrar_produto(prod4)
print(sistema.exibir_estoque())
print(prod1.remover_unidade(3))
print(sistema.exibir_estoque())
print(prod1.adicionar_novo(10))
print(sistema.exibir_estoque())
venda1 = Venda(p1, prod1, 2)
print(venda1.processar_venda(sistema))
print(sistema.exibir_estoque())
print(f"Valor no caixa: R${sistema.valor_caixa:.2f}")
print(venda1.cancelar_venda(sistema))
print(sistema.exibir_estoque())
print(venda1.processar_venda(sistema))
print(sistema.exibir_estoque())
venda2 = Venda(p1, prod1, 30)
print(venda2.processar_venda(sistema))
print(sistema.exibir_estoque())
venda3 = Venda(p1, prod1, 15)
print(venda3.processar_venda(sistema))
print(sistema.exibir_estoque())
print(f"Valor no caixa: R${sistema.valor_caixa:.2f}")