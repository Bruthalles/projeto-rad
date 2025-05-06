"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Base do sistema, cria o banco e a tabela inicial.
Se tá funcionando, não mexe. (Aprendi num tutorial de 2015 no youtube)]
"""

import sqlite3

def conectar_banco():
 return sqlite3.connect('clube.db')

def criar_tabela():
 conn = conectar_banco()
 cursor = conn.cursor()
 cursor.execute('''
    CREATE TABLE IF NOT EXISTS membros (
        
        nome TEXT NOT NULL,
        data_nascimento DATE,
        cpf TEXT PRIMARY KEY NOT NULL,
        email TEXT UNIQUE,
        data_cadastro DATE DEFAULT (date('now')),
        status TEXT CHECK(status IN ('Ativo', 'Inativo')) DEFAULT 'Ativo'
        )
    ''')
 conn.commit()

 def fechar_conexao():
    if conn:
        conn.close()
        conn = None