"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Pega a lista completa ou busca por ID específico.
Útil pra achar quem sumiu do pagamento da mensalidade.]
Sugestão: [Quando atualizamos as "areas" do cartao podera ter que mudar algumas coisas no codigo em geral(não só nesse) então avise para futuras modificaçoes]
"""

from models.db import conectar_banco

def obter_membros():
 conn = conectar_banco()
 cursor = conn.cursor()
 cursor.execute('SELECT * FROM membros')
 membros = cursor.fetchall()
 conn.close()
 return membros

def obter_membro_por_id(id_membro):
 conn = conectar_banco()
 cursor = conn.cursor()
 cursor.execute('SELECT * FROM membros WHERE id = ?', (id_membro,))
 membro = cursor.fetchone()
 conn.close()
 return membro