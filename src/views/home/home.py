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

    def change_page():
        root.destroy()
        Pg_Cadastro()

    #Scrollbar
    container = tk.Frame(root)
    container.pack(fill='both',expand=True)

    canvas = tk.Canvas(container,bg='white')

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side='right',fill='y')
    canvas.pack(side='left',fill='both',expand=True)

    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


    cadastrar = tk.Button(frame_botoes,text='Cadastrar',command=change_page)
    cadastrar.pack(padx=(5,12),pady=(5,12))

    lb = tk.Label(root,text='Lista de membros')
    lb.pack()

    section_membro = tk.Frame(container,padx=10,pady=10)
    section_membro.pack(fill='x')

    
    
    for membro in obter_membros():
        card = tk.Frame(section_membro,bd=2,relief='groove',bg='lightblue',padx=10,pady=10,width=250,height=150)
        card.pack(anchor='center',padx=10,pady=10)
        card.pack_propagate(False)

        id = tk.Label(card,text=f'ID: {membro['id']}',font=("Arial",12,'bold'),bg='lightblue')
        nome = tk.Label(card,text=f"Nome: {membro['nome'].capitalize()}",bg='lightblue',font=('Arial',12,'bold'))
        data_nascimento = tk.Label(card,text=f'Nascimento: {membro['data_nascimento']}',bg='lightblue',font=('Arial',12,'bold'))
        cpf = tk.Label(card,text=f'CPF: {membro['cpf']}',bg='lightblue',font=("Arial",12,'bold'))
        email = tk.Label(card,text=f'E-mail: {membro['email']}',bg='lightblue',font=("Arial",12,'bold'))
        cadastro = tk.Label(card,text=f'Data de Cadastro: {membro['data_cadastro']}',bg='lightblue',font=("Arial",12,'bold'))
        status = tk.Label(card,text=f'Status: {membro['status']}',bg='lightblue',font=("Arial",12,'bold'))

        id.pack(anchor='e')
        nome.pack(anchor='w')
        data_nascimento.pack(anchor='w')
        cpf.pack(anchor='w')
        email.pack(anchor='w')
        cadastro.pack(anchor='w')
        status.pack(anchor='w')



    root.mainloop()

    