# Problema 🔎 
O parque aquático AquaLife precisa gerenciar seus membros de forma digital

# 📌 Objetivo 🏆
Desenvolver um sistema com interfaces gráficas de 
gerenciamento com emissão de carteirinhas para integrantes do clube AquaLife club

---
# Como usar ?
Para entrar no sistema, é necessário do login de adminstrador, encontrado no arquivo .env em src/views/login/.env 

Execute o arquivo app.py em src/app.py e insira o nome e senha do admin. 

( VERSÃO NÃO EXECUTÁVEL PRECISARÁ INSTALAR DUAS LIBS ABAIXO )
pip install dotenv
pip install pillow

Após o login, será exibida a tela de carteirinhas. Clique no botão "Base de dados" para acessar e controlar o banco.

Ações de cadastrar, editar e remover serão salvas no arquivo relatorio_operacoes.txt em src/relatorio_operacoes.txt

# Estrutura do código fonte
├── src
    ├── relatorio_operacoes.txt
    ├── app.py
    ├── controllers
    │   ├── __init__.py
    │   ├── create_membro.py
    │   ├── delete_membro.py
    │   ├── logs.py
    │   ├── read_membro.py
    │   └── update_membro.py
    ├── icons
    │   ├── back.png
    │   ├── logo.png
    │   ├── reload.png
    │   └── user_icon.png
    ├── models
    │   ├── Membro.py
    │   ├── __init__.py
    │   ├── clube.db
    │   └── db.py
    └── views
    │   ├── __init__.py
    │   ├── cadastro
    │       └── cadastro.py
    │   ├── home
    │       ├── __init__.py
    │       └── home.py
    │   ├── login
    │       ├── .env
    │       ├── __init__.py
    │       └── login.py
    │   └── reports
    │       ├── __init__.py
    │       └── reports.py


# ⚙️ Requisitos

- Tkinter:
  - Criar uma interface gráfica simples e intuitiva utilizando Tkinter.
  
  - A interface deve conter ao menos três janelas: uma para o login, uma 
principal de gerenciamento e uma para relatórios.
  - Na janela principal, deve haver ao menos três funcionalidades de 
gerenciamento, como cadastro, edição e remoção de registros.
  - Botões devem ser configurados para interagir com o banco de dados 
(SQLite) de forma apropriada

- SQLite
  - O sistema deve utilizar um banco de dados SQLite local para armazenar 
os dados.
  - Criar uma tabela com ao menos 5 campos para armazenar as informações 
de uma entidade (por exemplo, cadastro de clientes e/ou produtos).
  - Implementar operações de CRUD (Criar, Ler, Atualizar, Apagar) na 
aplicação, utilizando SQL e Python para manipular os dados.

### Funcionalidades Obrigatórias:
- [X] Login: O sistema deve ter um login básico (não precisa de autenticação 
avançada) que permita o acesso ao sistema através de um nome de 
usuário.
- [X] Cadastro: Deve ser possível cadastrar, listar, editar e remover registros da 
tabela principal do banco de dados.
- [X] Relatórios: Criar uma funcionalidade de geração de relatórios básicos, 
que mostre os dados armazenados no banco de dados em uma nova 
janela.

 ### * Extras *
    - [ ] Salvar data de cadastro e remoção para manipulação de relatório.
    - [ ] Cadastrar apenas maiores de 18 anos
    - [ ] Adicionar validade para renovação de membro
    - [ ] Sistema de filtragem de buscas
    - [ ] Emitir aviso no sistema quando precisar renovar um cadastro
    - [ ] Lista de membros que precisam de renovação

---

# Equipe 

- Hugo Leonardo : Desenvolvedor (Banco de Dados e CRUD)
- Augusto Ivan : Desenvolvedor (Interfaces e CRUD)
- Fernando Matias : Desenvolvedor (Interfaces)
- Thalles Brumatti : Analista e Desenvolvedor (Modelagem, Documentação, Interfaces)



🔹 **Mantenedor:** *(Thalles Brumatti/@Bruthalles. Analista de Sistemas, Dev fullstack e gerente de projetos)*
