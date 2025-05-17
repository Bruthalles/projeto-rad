"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Remove membro permanentemente. 
Use com sabedoria não tem Ctrl+Z que te salve.]
"""
from controllers.read_membro import obter_membros
from controllers.logs import registrar_operacao
from models.db import BancoDeDados

bd = BancoDeDados()

def deletar_membro(id_membro,cpf_membro):
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 cursor.execute('DELETE FROM membros WHERE id = ?', (id_membro,))
 conn.commit()
 bd.fechar_conexao()
 registrar_operacao(f"Membro removido: ID {id_membro} (CPF: {cpf_membro})")
 return cursor.rowcount