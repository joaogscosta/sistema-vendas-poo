from flask import Flask, render_template, request, redirect, url_for, flash, session
from Nivel_1.classes import Sistema, Usuario, Cliente, Produto, Venda
from Nivel_2.funcoes_menu import meu_sistema
from Nivel_3.dados import salvar_dados

app = Flask(__name__)
app.secret_key = 'orientação_a_objetos'

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario_web():
    if request.method == 'POST':
        login = request.form.get('login').strip()
        senha = request.form.get('senha')

        if meu_sistema.buscar_usuario(login):
            flash(f"Erro: O login '{login}' já está em uso!", "danger")
            return redirect(url_for('cadastrar_usuario_web'))

        novo_u = Usuario(login, senha)
        meu_sistema.usuarios.append(novo_u)
        salvar_dados(meu_sistema) 

        flash(f"Usuário {login} cadastrado com sucesso!", "success")
        return redirect(url_for('login')) 

    return render_template('cadastro_usuario.html')

@app.route('/usuarios')
def listar_usuarios():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    # Passa a lista de usuários do sistema para o HTML
    return render_template('listar_usuarios.html', 
        usuario=session['usuario_logado'], 
        lista_usuarios=meu_sistema.usuarios)

@app.route('/excluir_usuario/<login_usuario>')
def excluir_usuario(login_usuario):
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    # Evita que o usuário logado exclua a si mesmo por acidente
    if session['usuario_logado'] == login_usuario:
        flash("Erro: Você não pode excluir o seu próprio usuário enquanto estiver logado!", "danger")
        return redirect(url_for('listar_usuarios'))

    # Remove o usuário usando o método que criamos no Nível 1
    meu_sistema.remover_usuario(login_usuario)
    
    # Atualiza o arquivo JSON usando o Nível 3
    salvar_dados(meu_sistema)
    
    flash(f"Usuário '{login_usuario}' removido com sucesso!", "success")
    return redirect(url_for('listar_usuarios'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_digitado = request.form.get('login').strip()
        senha_digitada = request.form.get('senha')

        usuario = meu_sistema.buscar_usuario(login_digitado)

        if usuario and usuario.senha == senha_digitada:
            session['usuario_logado'] = usuario.login 
            flash(f"{usuario.login} logado com sucesso!", "success")
            return redirect(url_for('index')) 
        else:
            flash("Login ou senha inválidos!", "danger")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None) 
    flash("Você saiu do sistema.", "info")
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect(url_for('login')) 
    
    return render_template('index.html', usuario=session['usuario_logado'])

@app.route('/perfil')
def perfil():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    return render_template('perfil.html', usuario=session['usuario_logado'])

# ==========================================
# ROTAS INTEGRADAS COM O NÍVEL 1 E NÍVEL 3:
# ==========================================

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form.get('nome').strip()
        id_cliente = request.form.get('id_cliente').strip()
        
        # 1. Instancia o objeto usando seu Nível 1 original
        novo_c = Cliente(id_cliente, nome)
        
        # 2. Adiciona na lista do sistema
        meu_sistema.clientes.append(novo_c)
        
        # 3. Salva no JSON usando seu Nível 3
        salvar_dados(meu_sistema)

        flash(f"Cliente {nome} cadastrado com sucesso!", "success")
        return redirect(url_for('cadastrar_cliente'))

    
    return render_template('cadastro_cliente.html', 
        usuario=session['usuario_logado'], 
        lista_clientes=meu_sistema.clientes)

@app.route('/excluir_cliente/<id_cliente>')
def excluir_cliente(id_cliente):
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    # 1. Procura o cliente na lista do seu Nível 1 e remove
    for cliente in meu_sistema.clientes:
        if cliente.id == id_cliente:
            meu_sistema.clientes.remove(cliente)
            break

    # 2. Salva as alterações no arquivo usando seu Nível 3
    salvar_dados(meu_sistema)
    
    flash("Cliente removido com sucesso!", "success")
    return redirect(url_for('cadastrar_cliente'))

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form.get('nome').strip()
        preco = float(request.form.get('preco').strip()) 
        qtd = int(request.form.get('quantidade').strip()) 

        # 1. Instancia o objeto usando seu Nível 1 original
        novo_p = Produto(nome, preco, qtd)
        
        # 2. Adiciona no estoque do sistema
        meu_sistema.estoque.append(novo_p)
        
        # 3. Salva no JSON usando seu Nível 3
        salvar_dados(meu_sistema)

        flash(f"Produto {nome} cadastrado com sucesso!", "success")
        return redirect(url_for('cadastrar_produto'))

    # CORREÇÃO AQUI: Passando meu_sistema.estoque para a tabela do HTML poder listar!
    return render_template('cadastro_produto.html', 
        usuario=session['usuario_logado'], 
        lista_produtos=meu_sistema.estoque)


@app.route('/excluir_produto/<nome_produto>')
def excluir_produto(nome_produto):
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    # 1. Procura o produto na lista do seu estoque e remove
    for produto in meu_sistema.estoque:
        if produto.nome == nome_produto:
            meu_sistema.estoque.remove(produto)
            break

    # 2. Salva as alterações no arquivo usando seu Nível 3
    salvar_dados(meu_sistema)
    
    flash(f"Produto '{nome_produto}' removido com sucesso!", "success")
    return redirect(url_for('cadastrar_produto'))

@app.route('/cadastrar_venda', methods=['GET', 'POST'])
def cadastrar_venda():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        id_cliente = request.form.get('id_cliente').strip()
        nome_produto = request.form.get('nome_produto').strip()
        qtd_venda = int(request.form.get('quantidade').strip())

        # Puxa os objetos completos do banco de dados do sistema usando os métodos do Nível 1
        cliente_obj = meu_sistema.buscar_cliente(id_cliente)
        produto_obj = meu_sistema.buscar_produto(nome_produto)

        if not cliente_obj or not produto_obj:
            flash("Erro: Cliente ou Produto não encontrado!", "danger")
            return redirect(url_for('cadastrar_venda'))

        # 1. Instancia a Venda passando os objetos reais
        nova_venda = Venda(cliente_obj, produto_obj, qtd_venda)

        # 2. Executa o método processar_venda da sua classe (que já dá baixa no estoque e mexe no caixa)
        sucesso, mensagem = nova_venda.processar_venda(meu_sistema)

        if sucesso:
            # 3. Se deu certo, adiciona no histórico de vendas do sistema
            meu_sistema.vendas.append(nova_venda)
            # 4. Salva no JSON através do seu Nível 3
            salvar_dados(meu_sistema)
            flash(mensagem, "success")
        else:
            flash(mensagem, "danger")

        return redirect(url_for('cadastrar_venda'))

    # Renderiza a página passando as três listas necessárias para a tela funcionar
    return render_template('cadastro_venda.html', 
        usuario=session['usuario_logado'], 
        lista_clientes=meu_sistema.clientes,
        lista_produtos=meu_sistema.estoque,
        lista_vendas=meu_sistema.vendas)



if __name__ == '__main__':
    app.run(debug=True)