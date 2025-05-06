"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Remove membro permanentemente. 
Use com sabedoria não tem Ctrl+Z que te salve.]
"""

from models.db import conectar_banco

def deletar_membro(id_membro):
 conn = conectar_banco()
 cursor = conn.cursor()
 cursor.execute('DELETE FROM membros WHERE id = ?', (id_membro,))
 conn.commit()
 conn.close()
 return cursor.rowcount