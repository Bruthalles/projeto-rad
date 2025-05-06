"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Responsável por cadastrar os novo membro. 
Cuidado com email repetido, o sistema não perdoa.]
"""
import sqlite3
from models.db import conectar_banco

def criar_membro(dados):
 conn = conectar_banco()
 cursor = conn.cursor()
 try:
        cursor.execute('''
            INSERT INTO membros (nome, idade, cpf, email)
            VALUES (?, ?, ?, ?)
        ''', (dados['nome'], dados['idade'], dados['endereco'], dados['email']))
        conn.commit()
        return cursor.lastrowid
 except sqlite3.IntegrityError:
        print("Erro: Email já cadastrado!")
        return None
 finally:
        conn.close()