"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Arquivo principal que roda o sistema.]
"""

from models.db import BancoDeDados
from models.Membro import Membro
from controllers.create_membro import criar_membro
from controllers.read_membro import obter_membros, obter_membro_por_id
from controllers.update_membro import atualizar_membro
from controllers.delete_membro import deletar_membro, limpar_tabela

if __name__ == "__main__":
    nome = input("digite nome do membro: ")
    data_nascimento = input("digite data de nascimento: ")
    email = input("digite email: ")
    cpf = input("digite cpf: ")
    
    membro = Membro(nome,data_nascimento,email,cpf)
    bd = BancoDeDados()

    bd.conectar_banco()
    bd.criar_tabela()
    
    
    id_novo = criar_membro(membro)
    print(f"Membro criado com ID: {id_novo}")
        
    print("\nLista de membros:")
    for membro in obter_membros():
        print(membro)

####FUNÇÃO TEMPORARIA PARA TESTES#######
    limpar_tabela()

   