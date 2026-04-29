from flask import Flask, render_template
from classes import Produto, Sistema

app = Flask(__name__)

# Criando dados para o site mostrar
sistema_web = Sistema()
p1 = Produto("Coca-Cola", 12, 5.50)
p2 = Produto("Batata Chips", 20, 8.00)
sistema_web.cadastrar_produto(p1)
sistema_web.cadastrar_produto(p2)

@app.route('/')
def index():
    # Enviamos a lista de produtos para o HTML
    return render_template('index.html', estoque=sistema_web.estoque)

if __name__ == '__main__':
    app.run(debug=True)
