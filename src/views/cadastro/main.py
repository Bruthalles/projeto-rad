from models.Membro import Membro
from controllers.create_membro import criar_membro
from controllers.read_membro import obter_membros, obter_membro_por_id
from controllers.update_membro import atualizar_membro
from controllers.delete_membro import deletar_membro, limpar_tabela
from tkinter import *

def Pg_Cadastro():
    app = Tk()
    app.geometry("600x500")
    app.title("Cadastro de membros")

    lb_nome = Label(app,text='Nome:',font=("Arial",18,'bold'))
    lb_nome.grid(column=0,row=4)

    fld_nome = Entry(app,width=30)
    fld_nome.grid(column=1,row=4)

    lbl_birth = Label(app,text='Data de Nascimento:',font=("Arial",18,'bold'))
    lbl_birth.grid(column=0,row=6)

    fld_birth = Entry(app,width=30)
    fld_birth.grid(column=1,row=6)

    lbl_cpf = Label(app,text='CPF:',font=("Arial",18,'bold'))
    lbl_cpf.grid(column=0,row=8)

    fld_cpf = Entry(app,width=30)
    fld_cpf.grid(column=1,row=8)

    lbl_email = Label(app,text="Email",font=("Arial",18,'bold'))
    lbl_email.grid(column=0,row=10)

    fld_email = Entry(app,width=30)
    fld_email.grid(column=1,row=10)

    aviso = Label(app,text="",font=("Arial",14,'bold'))
    aviso.grid(column=1,row=12)

    def get_membro():
        
        membro = Membro(nome=fld_nome.get(),
                        data_nascimento = fld_birth.get(),
                        cpf = fld_cpf.get(),
                        email = fld_email.get())
        

        if criar_membro(membro):
            aviso.config(text='Novo membro cadastrado!',fg='green')
        else: aviso.config(text='Este membro já existe',fg='red')
        
        
    cadastrar = Button(app,text='Salvar',bg='blue',fg='white',height=2,width=17,command=get_membro)
    cadastrar.grid(column=0,row=12)
    app.mainloop()
    