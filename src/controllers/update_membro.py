"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Atualiza informações do cadastro. 
Simples e auto explicativo POREM EU FIQUEI DUAS HORAS PROCURANDO UM ERRO NESSA MERDA E ERA A FALTA DE PONTO NO ".Join" AAAAAAAAA SOU BUCHA PROGRAMANDO]
Sugestão: [Quando atualizamos as "areas" do cartao podera ter que mudar algumas coisas no codigo em geral(não só nesse) então avise para futuras modificaçoes]
"""

from controllers.logs import registrar_operacao
from models.db import BancoDeDados
bd = BancoDeDados()

def atualizar_membro(id_membro, novos_dados):
    conn = bd.conectar_banco()
    cursor = conn.cursor()
    set_clause = ', '.join([f"{key} = ?" for key in novos_dados.keys()])
    valores = list(novos_dados.values())
    valores.append(id_membro)
    
    cursor.execute(f'''
        UPDATE membros
        SET {set_clause}
        WHERE id = ?
    ''', valores)
    conn.commit()
    bd.fechar_conexao()
    registrar_operacao(f"Membro atualizado: ID {id_membro}")
    return cursor.rowcount