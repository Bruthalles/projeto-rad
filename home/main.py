"""
Autor: [Hugo Leonardo Fonseca de Pinho]
Descrição: [Primeira versão da tela "principal" ainda não foi adicionado todas as funcionalidades e o banco de dados conectado 09/05/2025]

"""
import tkinter as tk
from tkinter import ttk

class InterfaceSimples:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("900x500")
        
        # Frame superior para botões
        self.frame_botoes = ttk.Frame(root)
        self.frame_botoes.pack(pady=10, fill='x')
        
        # Botões
        ttk.Button(self.frame_botoes, text="Cadastrar").pack(side='left', padx=5)
        ttk.Button(self.frame_botoes, text="Remover").pack(side='left', padx=5)
        ttk.Button(self.frame_botoes, text="Exportar").pack(side='left', padx=5)
        
        # Tabela de exibição
        self.criar_tabela()
        
        # Dados fictícios para demonstração
        self.inserir_dados_ficticios()

    def criar_tabela(self):
        # Configurar colunas
        colunas = ('nome', 'email', 'cpf', 'data_cadastro')
        
        self.tabela = ttk.Treeview(
            self.root,
            columns=colunas,
            show='headings',
            selectmode='browse'
        )
        
        # Configurar cabeçalhos
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('email', text='E-mail')
        self.tabela.heading('cpf', text='CPF')
        self.tabela.heading('data_cadastro', text='Data de Cadastro')
        
        # Configurar largura das colunas
        self.tabela.column('nome', width=200)
        self.tabela.column('email', width=250)
        self.tabela.column('cpf', width=150)
        self.tabela.column('data_cadastro', width=150)
        
        self.tabela.pack(fill='both', expand=True, padx=10, pady=5)

    def inserir_dados_ficticios(self):
        # Dados de exemplo
        dados = [
            ('João Silva', 'joao@email.com', '123.456.789-00', '2024-01-15'),
            ('Maria Souza', 'maria@email.com', '987.654.321-00', '2024-02-20'),
            ('Pedro Rocha', 'pedro@email.com', '456.789.123-00', '2024-03-05')
        ]
        
        for item in dados:
            self.tabela.insert('', 'end', values=item)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceSimples(root)
    root.mainloop()