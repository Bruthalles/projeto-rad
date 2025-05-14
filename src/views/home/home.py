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
        lb1 = tk.Label(section_membro,text=membro)
        lb1.pack(anchor='w')



    root.mainloop()

    