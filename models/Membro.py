# nome : str
#     - data_nascimento : date
#     - email : str 
#     - cpf : str
#     - data_cadastro : date 
#     + maior_de_idade(): bool 
#     + validar_cpf(): bool 

import datetime 
class Membro:

    nome: str
    data_nascimento: str 
    email: str
    cpf: str

    def __init__(self,nome,data_nascimento,email,cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento 
        self.email = email
        self.cpf = cpf

    