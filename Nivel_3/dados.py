import json
import os
from Nivel_1.classes import Cliente, Produto, Venda, Usuario

dados_crud = "database.json"

def salvar_dados(meu_sistema):
    dados = {
        
        "clientes": [
            # Ajustei aqui para 'id' e 'nome' ficarem iguais ao carregar_dados
            {"id": cliente.id, "nome": cliente.nome } for cliente in meu_sistema.clientes
        ],
        "produtos": [
            {"nome": produto.nome, "qtd": produto.qtd, "preco": produto.preco} for produto in meu_sistema.estoque
        ],
        "vendas": [
            {"cliente_id": venda.cliente.id, "produto_nome": venda.produto.nome, 
             "quantidade": venda.quantidade, "valor_total": venda.valor_total} for venda in meu_sistema.vendas
        ],
        "caixa": meu_sistema.valor_caixa,  # ADICIONEI ESTA LINHA PARA SALVAR O SALDO
        
        "usuarios": [
            {"login": u.login, "senha": u.senha} for u in meu_sistema.usuarios
            
            ]
    }
    
    try:
        # Recomendo usar encoding="utf-8" para não dar erro com acentos (ex: Coca-Cola)
        with open(dados_crud, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("\n[Sucesso] Dados salvos no banco!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados(meu_sistema):
    if os.path.exists(dados_crud):
        try:
            with open(dados_crud, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                
                # Carregar Clientes
                for c in dados.get("clientes", []):
                    meu_sistema.cadastrar_cliente(Cliente(c["id"], c["nome"]))
                
                # Carregar Produtos
                for p in dados.get("produtos", []):
                    meu_sistema.cadastrar_produto(Produto(p["nome"], p["qtd"], p["preco"]))
                
                # Restaurar o Saldo do Caixa
                meu_sistema.valor_caixa = dados.get("caixa", 0.0)
                
                # Restaurar histórico de vendas
                for v in dados.get("vendas", []):
                    c = meu_sistema.buscar_cliente(v["cliente_id"])
                    p = meu_sistema.buscar_produto(v["produto_nome"])
                    if c and p:
                        venda_salva = Venda(c, p, v["quantidade"])
                        meu_sistema.vendas.append(venda_salva)
                
                # --- CARREGAR USUÁRIOS (AGORA DENTRO DO BLOCO CORRETO) ---
                if "usuarios" in dados:
                    for u_data in dados["usuarios"]:
                        novo_usuario = Usuario(
                            u_data["login"], 
                            u_data["senha"], 
                            
                        )
                        meu_sistema.usuarios.append(novo_usuario)
            
            print("[Sucesso] Memória carregada com sucesso!")

        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    else:
        # Se o arquivo NÃO EXISTE, aí sim criamos o admin inicial
        print("[Aviso] Banco de dados não encontrado. Criando admin padrão...")
        admin_padrao = Usuario("admin", "123")
        meu_sistema.usuarios.append(admin_padrao)
        salvar_dados(meu_sistema)

    # Verificação extra: se o arquivo existia mas a lista de usuários veio vazia
    if not meu_sistema.usuarios:
        meu_sistema.usuarios.append(Usuario("admin", "123"))