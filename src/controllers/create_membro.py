"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Responsável por cadastrar os novo membro. 
Cuidado com email repetido, o sistema não perdoa.]
"""
import sqlite3
from models.db import BancoDeDados
bd = BancoDeDados()

def criar_membro(dados):
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 try:
        cursor.execute('''
            INSERT INTO membros (nome, data_nascimento, cpf, email)
            VALUES (?, ?, ?, ?)
        ''', (dados.nome, dados.data_nascimento, dados.cpf, dados.email))
        conn.commit()
        return cursor.lastrowid
 except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado!")
        return None
 finally:
        
        bd.fechar_conexao()