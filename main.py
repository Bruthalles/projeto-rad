"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Arquivo principal que roda o sistema.]
"""

from models.db import *
from controllers.create_membro import criar_membro
from controllers.read_membro import obter_membros, obter_membro_por_id
from controllers.update_membro import atualizar_membro
from controllers.delete_membro import deletar_membro

if __name__ == "__main__":
 criar_tabela()
    
    # Exemplo de uso
novo_membro = {
        'nome': 'Jair Luiz Messias Inácio Lulabolso da Silva',
        'idade': 78,
        'endereco': 'Av. do Caô , 171',
        'email': 'Politicameuszovos@gmail.com'
    }
    
id_novo = criar_membro(novo_membro)
print(f"Membro criado com ID: {id_novo}")
    
print("\nLista de membros:")
for membro in obter_membros():
    print(membro)

