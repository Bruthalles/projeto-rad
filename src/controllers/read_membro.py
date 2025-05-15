"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Pega a lista completa ou busca por ID específico.
Útil pra achar quem sumiu do pagamento da mensalidade.]
Sugestão: [Quando atualizamos as "areas" do cartao podera ter que mudar algumas coisas no codigo em geral(não só nesse) então avise para futuras modificaçoes]
"""

from models.db import BancoDeDados
bd = BancoDeDados()
def obter_membros():
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 cursor.execute('SELECT * FROM membros')

 #transforma tupla do banco para dicionario
 colunas = [desc[0] for desc in cursor.description]
 membros = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
 
 bd.fechar_conexao()
 return membros

def obter_membro_por_id(id_membro):
 conn = bd.conectar_banco()
 cursor = conn.cursor()
 cursor.execute('SELECT * FROM membros WHERE id = ?', (id_membro,))
 membro = cursor.fetchone()
 bd.fechar_conexao()
 return membro