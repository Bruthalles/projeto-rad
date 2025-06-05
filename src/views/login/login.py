from tkinter import * 
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from dotenv import load_dotenv
from views.home.home import Pg_Home

#carregando arquivo .env
load_dotenv()

#pegando usuario do arquivo .env 
NAME_USER = str(os.getenv("NOME_USER"))
PASS_USER = str(os.getenv("PASS_USER"))

# ""encapsulando"" a tela login
def Pg_Login():
    
    #definindo a estrutura e formas
    root = Tk()
    
    largura_janela = 900
    altura_janela = 500

    largura_tela = root.winfo_screenwidth()
    altura_Tela = root.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_Tela // 2) - (altura_janela // 2)
    root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

    frame = Frame(root)
    frame.pack(expand=True)
    frame.place(relx=0.5,rely=0.5,anchor='center')

    root.title("Emissão de Carteirinhas - Login")

    #Componentes
    img_logo = Image.open('src/icons/logo.png')
    logo_resize = img_logo.resize((380,120))
    logo = ImageTk.PhotoImage(logo_resize)

    txt_logo = Label(root,image=logo)
    txt_logo.pack(pady=(20,40))

    txt_usr = Label(root,text='Usuário',font=("Arial",14))
    txt_usr.pack(pady=0,padx=(0,105))

    field_usr = Entry(root,width=20,bg="#0C94B6",fg='white')
    field_usr.pack(pady=(0,20))

    txt_senha = Label(root, text="Senha",font=("Arial",14))
    txt_senha.pack(pady=0,padx=(0,115))

    field_senha = Entry(root,width=20,bg="#0C94B6",fg='white',show="°")
    field_senha.pack(pady=(0,20))

    #pegando valor do elemento Entry
    def get_user():
        nm_user = str(field_usr.get())
        ps_user = str(field_senha.get())
        return nm_user,ps_user

    #validação simples e troca de tela
    def validar_usuario(in_user,in_pass):
        
        if(in_user == NAME_USER and in_pass == PASS_USER):
            root.destroy()
            Pg_Home()
        else: 
            messagebox.showerror("Erro","Usuário inválido")
    
    #simplificando a função para ser chamada
    def login():
        nm_user , ps_user = get_user()
        validar_usuario(nm_user,ps_user)

    #parametro command deve receber uma função sem parenteses para não executar imediatamente
    entrar = Button(root,text="Entrar",height=2,width=17,bg="#FBFF00",fg="black",font=("Arial",11,"bold"),command=login)
    entrar.pack(pady=(20,50))

    root.mainloop()