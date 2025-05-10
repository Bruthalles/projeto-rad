from tkinter import * 
import os
from dotenv import load_dotenv
from views.home.main import Pg_Home

#carregando arquivo .env
load_dotenv()

#pegando usuario do arquivo .env 
user_name = str(os.getenv("NOME_USER"))
pass_user = str(os.getenv("PASS_USER"))

def Pg_Login():
        
    pg_login = Tk()
    pg_login.geometry('400x400')
    frame = Frame(pg_login)
    frame.pack(expand=True)
    frame.place(relx=0.5,rely=0.5,anchor='center')

    pg_login.title("Emissão de Carteirinhas - Login")

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

    def get_user():

        nm_user = str(field_usr.get())
        ps_user = str(field_senha.get())
        return nm_user,ps_user

    def validar_usuario(in_user,in_pass):
        
        if(in_user == user_name and in_pass == pass_user):
            aviso.config(text="Bem vindo !",fg="green")
            pg_login.destroy()
            Pg_Home()
        else: 
            aviso.config(text="Usuario incorreto",fg="red")
        
    def login():
        nm_user , ps_user = get_user()
        validar_usuario(nm_user,ps_user)

    entrar = Button(pg_login,text="Entrar",height=2,width=17,bg="blue",fg="white",font=("Arial",11,"bold"),command=login)
    entrar.pack(pady=(20,50))

    pg_login.mainloop()