"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Remove membro permanentemente. 
Use com sabedoria não tem Ctrl+Z que te salve.]
"""
from controllers.read_membro import obter_membros
from models.db import BancoDeDados
bd = BancoDeDados()
def deletar_membro(id_membro):
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 cursor.execute('DELETE FROM membros WHERE id = ?', (id_membro,))
 print("\nLista de membros:")
 for membro in obter_membros():
    print(membro)
 conn.commit()
 bd.fechar_conexao()
 return cursor.rowcount