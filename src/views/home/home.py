import tkinter as tk
from tkinter import ttk
from controllers.read_membro import obter_membros
from views.cadastro.augustocadastro import Pg_Cadastro

def Pg_Home():
    root = tk.Tk()
    root.title("Membros cadastrados")
    root.geometry('900x500')
    
    frame_botoes = tk.Frame(root)
    frame_botoes.pack(padx=10,pady=10)

    cadastrar = tk.Button(frame_botoes,text='Cadastrar',command=Pg_Cadastro)
    cadastrar.pack(padx=(5,12),pady=(5,12))

    lb = tk.Label(root,text='Lista de membros')
    lb.pack()

    section_membro = tk.Frame(root,bg='lightyellow',padx=10,pady=10)
    section_membro.pack(fill='x')

    for membro in obter_membros():

        test = tk.Label()
        card = tk.Frame(section_membro,bd=2,relief='groove',bg='lightblue')
        card.pack(anchor='w')

        nome = tk.Label(card,text=f"Nome: {membro['nome']}",font=('Arial',12,'bold'))
        data_nascimento = tk.Label(card,text=f'Nascimento: {membro['data_nascimento']}',font=('Arial',12,'bold'))
        cpf = tk.Label(card,text=f'CPF: {membro['cpf']}',font=("Arial",12,'bold'))
        email = tk.Label(card,text=f'E-mail: {membro['email']}',font=("Arial",12,'bold'))
        nome.pack(anchor='w')
        data_nascimento.pack(anchor='w')
        cpf.pack(anchor='w')
        email.pack(anchor='w')



    root.mainloop()

    