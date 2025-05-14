"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Base do sistema, cria o banco e a tabela inicial.
Se tá funcionando, não mexe. (Aprendi num tutorial de 2015 no youtube)]
Copiloto: Thalles Brumatti :D editando algumas coisas...
"""

import sqlite3,os
class BancoDeDados:

    def __init__(self):
        self.conn = None
    
    
    def conectar_banco(self):
        #criando db no mesmo diretorio
        path = os.path.join(os.path.dirname(__file__),'clube.db')
        self.conn = sqlite3.connect(path)
        return self.conn
    
    
    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS membros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento DATE,
                cpf TEXT NOT NULL,
                email TEXT UNIQUE,
                data_cadastro DATE DEFAULT (date('now')),
                status TEXT CHECK(status IN ('Ativo', 'Inativo')) DEFAULT 'Ativo'
                )
            ''')
        self.conn.commit()

    
    def fechar_conexao(self):
        self.conn.close()
        self.conn = None