"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Responsável por cadastrar os novo membro. 
Cuidado com email repetido, o sistema não perdoa.]
"""
import sqlite3
from controllers.logs import registrar_operacao
from models.db import BancoDeDados
bd = BancoDeDados()

def criar_membro(dados):
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 try:
        cursor.execute('''
            INSERT INTO membros (nome, data_nascimento, cpf, email, atestado)
            VALUES (?, ?, ?, ?, ?)
        ''', (dados.nome, dados.data_nascimento, dados.cpf, dados.email,dados.atestado))
        conn.commit()
        
        if cursor.lastrowid:
              registrar_operacao(f"Membro criado: {dados.nome} (CPF: {dados.cpf})")
        return True
 except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado!")
        return None
 finally:
        
        bd.fechar_conexao(conn)