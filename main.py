from classes import Sistema, Cliente, Produto, Venda


#Cria Clientes
p1 = Cliente(1010, "Joao")
p2 = Cliente(1020, "Maria")
p3 = Cliente(1030, "Pedro")
p4 = Cliente(1040, "Ana")

#Cadastra clientes
sistema = Sistema()
sistema.cadastrar_cliente(p1)
sistema.cadastrar_cliente(p2)
sistema.cadastrar_cliente(p3)

#Cria produtos
prod1 = Produto("Coca-cola", 10, 5.0)
prod2 = Produto("Pepsi", 15, 4.5)

#Cadastra produtos
sistema.cadastrar_produto(prod1)
sistema.cadastrar_produto(prod2) 

#TESTES

print(prod1.visualizar_produto())
print(prod2.visualizar_produto())

#Manipulando estoque
print("\n--- Adicionando estoque de Coca ---")
prod1.adicionar_novo(5) 
print(prod1.visualizar_produto())

print("\n--- Processando Venda 1 ---")
venda1 = Venda(p1, prod1, 2)
print(venda1.processar_venda(sistema))
print(f"Caixa: R${sistema.valor_caixa:.2f}")

print("\n--- Cancelando Venda 1 ---")
print(venda1.cancelar_venda(sistema))
print(f"Caixa atualizado: R${sistema.valor_caixa:.2f}")

print("\n--- Tentando venda sem estoque ---")
venda_absurda = Venda(p1, prod1, 100)
print(venda_absurda.processar_venda(sistema))