from Nivel_1.classes import Cliente, Produto, Venda, Sistema
from Nivel_3.dados import   carregar_dados, salvar_dados


meu_sistema = Sistema()
carregar_dados(meu_sistema)

def cadastro_cliente():
 
    id_cliente = input("Digite o id do cliente:")
    nome_cliente = input("Digite o nome do cliente:").strip().title()
    novo_cliente = Cliente(id_cliente, nome_cliente)
    meu_sistema.cadastrar_cliente(novo_cliente)
    print("Cliente cadastrado!")
    input("\nPressione Enter para continuar...")
def visualiza_cliente():
    if not meu_sistema.clientes:
        print("Nenhum cliente cadastrado!")
    else:    
        for cliente in meu_sistema.clientes:
            print(cliente.visualizar_cliente())
    input("\nPressione Enter para continuar...")                 
    
def excluir_cliente():
    id_cliente = input("Digite o id do cliente a ser removido:")
    meu_sistema.remover_cliente(id_cliente)
    print("Cliente removido!")
    input("\nPressione Enter para continuar...")

def cadastro_produto():
    nome_produto = input("Digite o nome do produto:").strip().title()
    qtd_produto = int(input("Digite a quantidade do produto:"))
    preço_produto = float(input("Digite o preço do produto:"))
    novo_produto = Produto(nome_produto, qtd_produto, preço_produto)
    meu_sistema.cadastrar_produto(novo_produto)
    print("Produto cadastrado!")
    input("\nPressione Enter para continuar...")

def visualiza_produto():
     if not meu_sistema.estoque:
            print("Nenhum produto cadastrado!")
     else:       
            for produto in meu_sistema.estoque:
                print(produto.visualizar_produto())
      
            input("\nPressione Enter para continuar...")     
    
def adiciona_qtd():
    nome_produto = input("Digite o nome do produto para adicionar quantidade:").strip().title()
    produto = meu_sistema.buscar_produto(nome_produto)
    if produto:
            quantidade_nova = int(input("Digite a quantidade a ser adicionada:"))
            produto.adicionar_novo(quantidade_nova)
            print("Quantidade adicionada!")
    input("\nPressione Enter para continuar...")

def remove_qtd():
    nome_produto = input("Digite o nome do produto para remover quantidade:").strip().title()
    produto = meu_sistema.buscar_produto(nome_produto)
    if produto:
                quantidade_a_remover = int(input("Digite a quantidade a ser removida:"))
                if produto.remover_unidade(quantidade_a_remover):
                    print("Unidades removidas!")
                else:
                    print("QUANTIDADE EXCEDIDA!!")
                    
                input("\nPressione Enter para continuar...")    

def processa_venda():
    id_cliente = input("Digite o ID do cliente: ")
    cliente = meu_sistema.buscar_cliente(id_cliente)
            
    if cliente:
            print(f"Cliente encontrado: {cliente.nome}")
            nome_produto = input("Digite o nome do produto: ").strip().title()
            produto = meu_sistema.buscar_produto(nome_produto)
                
            if produto:
                quantidade = int(input(f"Quantidade de {produto.nome}: "))
                    
                
                nova_venda = Venda(cliente, produto, quantidade)
                    
                resultado_venda = nova_venda.processar_venda(meu_sistema)
                    
                sucesso, mensagem = resultado_venda
                print(mensagem)
                
                if sucesso:
                    meu_sistema.vendas.append(nova_venda)
            else:
                    print("Erro: Produto não encontrado!")
    else:
        print("Erro: Cliente não cadastrado! Cadastre-o na opção 1 primeiro.")
        
    input("\nPressione Enter para continuar...")  
               
def historico_vendas(sistema):
   
    print(f"{'HISTÓRICO DE VENDAS':^50}")
   
    if not meu_sistema.vendas:
        print("\nNenhuma venda realizada até o momento.")
    else:
        # Cabeçalho da tabela
        print(f"{'Cliente':<15} | {'Produto':<15} | {'Qtd':<5} | {'Total':<10}")
        print("-" * 50)
        
        for venda in sistema.vendas:
            nome_cliente = venda.cliente.nome
            nome_produto = venda.produto.nome
            qtd = venda.quantidade
            total = venda.valor_total
            
            print(f"{nome_cliente:<15} | {nome_produto:<15} | {qtd:<5} | R$ {total:>8.2f}")
    
    print("="*50)
    input("\nPressione Enter para voltar ao menu...")  
      
def cancela_venda():
    print("Cancelar venda")
    cliente_id = input("Digite o id do cliente para cancelar a venda:")
    cliente = meu_sistema.buscar_cliente(cliente_id)
    if cliente:
            nome_produto = input("Digite o nome do produto para cancelar a venda:").strip().title()
            produto = meu_sistema.buscar_produto(nome_produto)
            if produto:
                quantidade_cancelar = int(input("Digite a quantidade a ser cancelada:"))
                produto.adicionar_novo(quantidade_cancelar)
                valor_cancelamento = quantidade_cancelar * produto.preço
                meu_sistema.valor_caixa -= valor_cancelamento
                print(f"Venda cancelada! Valor reembolsado: R${valor_cancelamento:.2f}")
    input("\nPressione Enter para continuar...")     
    
def saldo_caixa():
    print(f"Saldo atual do caixa: R${meu_sistema.valor_caixa:.2f}")
    
    input("\nPressione Enter para continuar...")     
    
def sair(): 
    print("Saindo do sistema...")
    
 
                  
def exibi_menu():
    print("\nMenu Principal:")
    print("1 - Cadastrar Cliente")
    print("2 - Visualizar Clientes")
    print("3 - Excluir Cliente")
    print("4 - Cadastrar Produto")
    print("5 - Visualizar Produtos")
    print("6 - Adicionar Quantidade ao Produto")
    print("7 - Remover Quantidade do Produto")
    print("8 - Processar Venda")
    print("9 - Cancelar Venda")
    print("10 - Histórico de Vendas")
    print("11 - Ver Saldo do Caixa")
    print("12 - Sair") 
    
    
def menu_principal():
    while True: 
     exibi_menu()
     opcao_1 = input("Escolha uma opçao:")
     match opcao_1:
        case "1":
            cadastro_cliente()
        case "2":
            visualiza_cliente()
        case "3":
            excluir_cliente()   
        case "4":
            cadastro_produto()
        case "5":
            visualiza_produto()
        case "6":
            adiciona_qtd()
        case "7":
            remove_qtd()
        case "8":
            processa_venda()
        case "9":
            cancela_venda()
        case "10":
            historico_vendas(meu_sistema)
        case "11":
            saldo_caixa()
        case "12":
            salvar_dados(meu_sistema)  
            sair()
            break
        case _:
            print("Opção inválida, tente novamente!")                   
    
def menu_iniciar():
    print( "1 - Iniciar ")
    print( "2 - Sair ")
    while True:
      opcao = input("Digite a opção desejada:")
      match opcao:
        case "1":
            print("Iniciando o sistema...")
            menu_principal()
        case "2":
            sair()
            salvar_dados(meu_sistema)
            break
        case _:
            print("Opção inválida, tente novamente!")  
            
            
