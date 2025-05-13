"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Primeira versão da tela "principal" ainda não foi adicionado todas as funcionalidades e o banco de dados conectado 09/05/2025]

"""
from models.db import BancoDeDados
from controllers.read_membro import obter_membros
import tkinter as tk
from tkinter import ttk
from views.cadastro.main import Pg_Cadastro

def Pg_Home():
    root = tk.Tk()
    banco = BancoDeDados()
    banco.conectar_banco()
    banco.criar_tabela()
    app = InterfaceMain(root)
    root.mainloop()

class InterfaceMain:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("900x500")
        
        # Frame superior para botões
        self.frame_botoes = ttk.Frame(root)
        self.frame_botoes.pack(pady=10, fill='x')
        
        # Botões
        ttk.Button(self.frame_botoes, text="Cadastrar",command=Pg_Cadastro).pack(side='left', padx=5)
        ttk.Button(self.frame_botoes, text="Remover").pack(side='left', padx=5)
        ttk.Button(self.frame_botoes, text="Exportar").pack(side='left', padx=5)
        
        # Tabela de exibição
        self.criar_tabela()
        
        # Dados fictícios para demonstração
        self.inserir_dados_ficticios()

    def criar_tabela(self):
        # Configurar colunas
        colunas = ('nome', 'data_nascimento', 'cpf', 'email')
        
        self.tabela = ttk.Treeview(
            self.root,
            columns=colunas,
            show='headings',
            selectmode='browse'
        )
        
        # Configurar cabeçalhos
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('data_nascimento', text='Data de nascimento')
        self.tabela.heading('cpf', text='CPF')
        self.tabela.heading('email', text='Email')
        
        # Configurar largura das colunas
        self.tabela.column('nome', width=200)
        self.tabela.column('data_nascimento', width=250)
        self.tabela.column('cpf', width=150)
        self.tabela.column('email', width=150)
        
        self.tabela.pack(fill='both', expand=True, padx=10, pady=5)

    def inserir_dados_ficticios(self):
        # Dados de exemplo
        dados =  obter_membros()
        #[
        #     ('João Silva', '2004-01-15' , '123.456.789-00' , 'joao@email.com'),
        #     ('Maria Souza', '1980-9-12', '987.654.321-00', 'maria@email.com'),
        #     ('Pedro Rocha', '1945-8-5', '456.789.123-00', 'pedro@email.com'),
        #     ('Thalles Brumatti','2005-4-2','333.222.111-01','thalles@dev.com')
        # ]
        self.tabela.delete(*self.tabela.get_children())
        for item in dados:
            self.tabela.insert('', 'end', values=item)
