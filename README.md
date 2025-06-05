<h1 align="center">💧 AquaLife Club – Sistema de Gerenciamento de Membros</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-%20finalizado-darkgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/interface-Tkinter-blue.svg" alt="Interface">
  <img src="https://img.shields.io/badge/banco-SQLite-lightblue.svg" alt="Banco de dados">
</p>

---

## 🔍 Problema
O parque aquático <strong>AquaLife</strong> precisa modernizar a gestão de seus membros, migrando para um sistema digital.

## 🎯 Objetivo
Desenvolver um sistema com <strong>interfaces gráficas</strong> para gerenciamento de membros, com <strong>emissão de carteirinhas</strong> personalizadas para os integrantes do clube AquaLife.

---

## 🚀 Como Usar

```bash
# 1. Acesse o login de administrador
# O arquivo está em:
src/views/login/.env

⚠️ # Inicialmente os arquivos de relatório e do banco não serão vistos pois eles são criados durante a execução

# 2. Execute o sistema
python src/app.py

# 3. Se necessário, instale as dependências:
pip install python-dotenv
pip install pillow

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

```
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
- ✔️ Login: O sistema deve ter um login básico (não precisa de autenticação 
avançada) que permita o acesso ao sistema através de um nome de 
usuário.
- ✔️ Cadastro: Deve ser possível cadastrar, listar, editar e remover registros da 
tabela principal do banco de dados.
- ✔️ Relatórios: Criar uma funcionalidade de geração de relatórios básicos, 
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
