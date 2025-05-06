from models.Usuario import Usuario

if __name__ == '__main__':
    admin = Usuario
    user = input('digite o nome de usuário: ')
    senha = input("digete a senha: ")
    
    admin.validar_usuario(admin,user,senha)