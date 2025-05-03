from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    senha: str

    def validar_usuario(self,nome,senha)-> bool:
        if (nome == self.nome and senha == self.senha):
            return True
        else: 
            return "Usuario inválido!"
