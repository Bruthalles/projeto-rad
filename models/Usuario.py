import os
from dotenv import load_dotenv

#carregando arquivo .env
load_dotenv()

#pegando usuario do arquivo .env 
user_name = os.getenv("NOME_USER")
pass_user = os.getenv("PASS_USER")
class Usuario:

    usuario = user_name
    senha = pass_user

    def validar_usuario(self,in_user,in_pass)-> bool:
        if (in_user == self.usuario and in_pass == self.senha):
            print(" tela principal")
        else: 
            print("Usuario inválido!")