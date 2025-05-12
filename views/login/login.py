from tkinter import * 
import os
from dotenv import load_dotenv
from views.home.main import Pg_Home

#carregando arquivo .env
load_dotenv()

#pegando usuario do arquivo .env 
user_name = str(os.getenv("NOME_USER"))
pass_user = str(os.getenv("PASS_USER"))

# ""encapsulando"" a tela login
def Pg_Login():
    
    #definindo a estrutura e formas
    pg_login = Tk()
    pg_login.geometry('900x500')
    frame = Frame(pg_login)
    frame.pack(expand=True)
    frame.place(relx=0.5,rely=0.5,anchor='center')

    pg_login.title("Emissão de Carteirinhas - Login")

    #Componentes
    txt_login = Label(pg_login,text="Login",font=("Arial",20))
    txt_login.pack(pady=(20,40))

    txt_usr = Label(pg_login,text='Usuário')
    txt_usr.pack(pady=0,padx=(0,115))

    field_usr = Entry(pg_login,width=20)
    field_usr.pack(pady=(0,20))

    txt_senha = Label(pg_login, text="Senha")
    txt_senha.pack(pady=0,padx=(0,125))

    field_senha = Entry(pg_login,width=20)
    field_senha.pack(pady=(0,20))

    aviso = Label(pg_login,text="",font=("Arial",12,"bold"))
    aviso.pack(pady=(5,5))

    #pegando valor do elemento Entry
    def get_user():
        nm_user = str(field_usr.get())
        ps_user = str(field_senha.get())
        return nm_user,ps_user

    #validação simples e troca de tela
    def validar_usuario(in_user,in_pass):
        
        if(in_user == user_name and in_pass == pass_user):
            aviso.config(text="Bem vindo !",fg="green")
            pg_login.destroy()
            Pg_Home()
        else: 
            aviso.config(text="Usuario incorreto",fg="red")
    
    #simplificando a função para ser chamada
    def login():
        nm_user , ps_user = get_user()
        validar_usuario(nm_user,ps_user)

    #parametro command deve receber uma função sem parenteses para não executar imediatamente
    entrar = Button(pg_login,text="Entrar",height=2,width=17,bg="blue",fg="white",font=("Arial",11,"bold"),command=login)
    entrar.pack(pady=(20,50))

    pg_login.mainloop()