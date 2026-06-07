# 💰 SISTEMA DE GERENCIAMENTO COMERCIAL

Foi desenvolvido um sistema web completo, para gerenciamento de produtos, clientes e vendas, focado em organização e facilidade de uso.

---

## 🚀 Sobre o projeto

O maior objetivo do projeto era matar uma dificuldade real que meus parentes tinham com a gestao de sua mercearia.

---

## Funcionalidades do Sistema

* **Controle de Estoque:** Com aviso de estoque, é possivel barrar uma compra.
* **Gerenciamento de clientes:** Listagem e Exclusão direto pelo site.
* **Fluxo de Vendas:** Baixa automaticamente o estoque quando uma venda é realizada.
* **Controle de Acesso:** Login e gerenciamento de usuários.

---

## 🏗️ Estrutura e Arquitetura do Projeto

Como este projeto foi desenvolvido como parte de uma disciplina acadêmica, o código foi rigorosamente estruturado em camadas (Níveis) para garantir a separação de responsabilidades:

* **Nível 1 (Modelos/Classes):** Onde está a base do projeto, tudo ainda roda por terminal.
* **Nível 2 (Terminal):** Criação do CRUD.

* **Nível 3 (Persistência):** Onde foi implantado o banco de dados JSON.

* **Nível 4 Interface Web (Flask):** Onde o projeto deixou de ser só terminal e ganhou um site.

---

## 💻 Como Executar o Projeto

Este sistema foi projetado para ser versátil e pode ser executado de três formas distintas, dependendo do objetivo:

Antes de escolher a forma de rodar, faça o download do projeto clonando este repositório no seu terminal:

```bash
git clone [https://github.com/joaogscosta/sistema-vendas-poo.git]

cd projeto-vendas

### 1. Execução via Web (Flask)
É a versão completa e atual do sistema, com interface gráfica rodando direto no navegador.
* Instale o Flask: `pip install flask`
* Execute o arquivo de rotas: `python route.py`
* Acesse no navegador: `http://127.0.0.1:5000`

### 2. Execução via Terminal (Modo Interativo)
Permite rodar as funções de CRUD (Cadastro, Consulta, Atualização e Deleção) direto pelo terminal, usando a lógica desenvolvida no Nível 2.
* Execute o arquivo principal do terminal: `python main.py`

### 
Permite instanciar as classes puras do Nível 1 diretamente no console interativo do Python para realizar testes de bancada na lógica de negócios (como testar um método de venda ou validação de produto perecível).
Para rodar o teste, em nivel 1, execute test_sistema.py
