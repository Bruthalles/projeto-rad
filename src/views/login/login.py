from tkinter import * 
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from dotenv import load_dotenv
from views.home.home import Pg_Home

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
    img_logo = Image.open('src/icons/logo.png')
    logo_resize = img_logo.resize((380,120))
    logo = ImageTk.PhotoImage(logo_resize)

    txt_logo = Label(pg_login,image=logo)
    txt_logo.pack(pady=(20,40))

    txt_usr = Label(pg_login,text='Usuário',font=("Arial",14))
    txt_usr.pack(pady=0,padx=(0,105))

    field_usr = Entry(pg_login,width=20,bg="#0C94B6",fg='white')
    field_usr.pack(pady=(0,20))

    txt_senha = Label(pg_login, text="Senha",font=("Arial",14))
    txt_senha.pack(pady=0,padx=(0,115))

    field_senha = Entry(pg_login,width=20,bg="#0C94B6",fg='white')
    field_senha.pack(pady=(0,20))

    #pegando valor do elemento Entry
    def get_user():
        nm_user = str(field_usr.get())
        ps_user = str(field_senha.get())
        return nm_user,ps_user

    #validação simples e troca de tela
    def validar_usuario(in_user,in_pass):
        
        if(in_user == user_name and in_pass == pass_user):
            pg_login.destroy()
            Pg_Home()
        else: 
            messagebox.showerror("Erro","Usuário inválido")
    
    #simplificando a função para ser chamada
    def login():
        nm_user , ps_user = get_user()
        validar_usuario(nm_user,ps_user)

    #parametro command deve receber uma função sem parenteses para não executar imediatamente
    entrar = Button(pg_login,text="Entrar",height=2,width=17,bg="#FBFF00",fg="black",font=("Arial",11,"bold"),command=login)
    entrar.pack(pady=(20,50))

    pg_login.mainloop()