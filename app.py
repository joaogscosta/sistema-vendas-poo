from flask import Flask, render_template, request, redirect, url_for, flash
from Nivel_1.classes import Sistema, Usuario, Cliente, Produto
from Nivel_2.funcoes_menu import meu_sistema
from Nivel_3.dados import salvar_dados
from flask import session


app = Flask(__name__)
app.secret_key = 'orientação_a_objetos'

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario_web():
    if request.method == 'POST':
        login = request.form.get('login').strip()
        senha = request.form.get('senha')

        # 1. A MESMA TRAVA DO NÍVEL 2:
        if meu_sistema.buscar_usuario(login):
            flash(f"Erro: O login '{login}' já está em uso!", "danger")
            return redirect(url_for('cadastrar_usuario_web'))

        # 2. SE PASSOU PELA TRAVA, CRIA E SALVA:
        novo_u = Usuario(login, senha)
        meu_sistema.usuarios.append(novo_u)
        salvar_dados(meu_sistema) # Garante que salve no JSON

        flash(f"Usuário {login} cadastrado com sucesso!", "success")
        return redirect(url_for('login')) # Manda para a tela de login

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_digitado = request.form.get('login').strip()
        senha_digitada = request.form.get('senha')

        # 1. Busca o usuário no sistema
        usuario = meu_sistema.buscar_usuario(login_digitado)

        # 2. Verifica se o usuário existe E se a senha está correta
        if usuario and usuario.senha == senha_digitada:
            session['usuario_logado'] = usuario.login # "Entrega o crachá"
            flash(f"{usuario.login} logado com sucesso!", "success")
            return redirect(url_for('index')) # Manda para a página principal
        else:
            flash("Login ou senha inválidos!", "danger")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None) # "Recolhe o crachá"
    flash("Você saiu do sistema.", "info")
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect(url_for('login')) # Se não tiver crachá, vai para o login
    
    return render_template('index.html', usuario=session['usuario_logado'])

@app.route('/perfil')
def perfil():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    return render_template('perfil.html', usuario=session['usuario_logado'])

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form.get('nome').strip()
        id_cliente = request.form.get('id_cliente').strip()
        
        # Lógica para cadastrar cliente (exemplo simplificado)
        flash(f"Cliente {nome} cadastrado com sucesso!", "success")
        return redirect(url_for('index'))

    return render_template('cadastro_cliente.html', usuario=session['usuario_logado'])

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form.get('nome').strip()
        preco = request.form.get('preco').strip()
        qtd = request.form.get('quantidade').strip()

        # Lógica para cadastrar produto (exemplo simplificado)
        flash(f"Produto {nome} cadastrado com sucesso!", "success")
        return redirect(url_for('index'))

    return render_template('cadastro_produto.html', usuario=session['usuario_logado'])

if __name__ == '__main__':
    app.run(debug=True)