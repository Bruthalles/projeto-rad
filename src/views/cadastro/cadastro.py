import tkinter as tk
from tkinter import ttk, messagebox
from models.Membro import Membro
from models.db import BancoDeDados
from controllers.create_membro import criar_membro
from controllers.read_membro import obter_membros, obter_membro_por_id
from controllers.update_membro import atualizar_membro
from controllers.delete_membro import deletar_membro, limpar_tabela

def Pg_Cadastro():
    root = tk.Tk()
    banco = BancoDeDados()
    banco.conectar_banco()
    banco.criar_tabela()
    app = CadastroApp(root)
    root.mainloop()

class CadastroApp:

    def change_page(self):
        self.root.destroy()
        
        from views.home.home import Pg_Home #evita import circular
        Pg_Home()

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("1000x700")

        # Variável para controlar se o formulário está visível
        self.formulario_visivel = False
        
        # Frame do formulário de cadastro (inicialmente oculto)
        self.frame_formulario = tk.Frame(root)

        # Frame superior com botões
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=10)
        
        self.btn_membros = tk.Button(self.frame_botoes, text="Membros",command=self.change_page)
        self.btn_membros.pack(side=tk.LEFT, padx=5)

        self.btn_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.mostrar_formulario)
        self.btn_cadastrar.pack(side=tk.LEFT, padx=5)
        
        self.btn_remover = tk.Button(self.frame_botoes, text="Remover", command=self.remover_usuario)
        self.btn_remover.pack(side=tk.LEFT, padx=5)
        
        self.btn_exportar = tk.Button(self.frame_botoes, text="Exportar")
        self.btn_exportar.pack(side=tk.LEFT, padx=5)
        
        # Frame da lista de registros
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview para exibir os registros
        self.tree = ttk.Treeview(self.frame_lista, columns=("Nome","Data de Nascimento", "CPF", "Email", "Data Cadastro"), show="headings")
        
        # Configurar cabeçalhos
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Data de Nascimento",text="Data de Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Data Cadastro", text="Data Cadastro")
        
        # Configurar colunas
        self.tree.column("Nome", width=200)
        self.tree.column("Data de Nascimento", width=200)
        self.tree.column("CPF", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Data Cadastro", width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Frame para botões de ação (alternativa à coluna Ações)
        self.frame_acoes = tk.Frame(root)
        self.frame_acoes.pack(pady=5)
        
        # Botão de editar (para o item selecionado)
        self.btn_editar_selecionado = tk.Button(
            self.frame_acoes, 
            text="Editar Selecionado", 
            command=self.editar_selecionado,
            bg='#99ccff',
            width=15
        )
        self.btn_editar_selecionado.pack(side=tk.LEFT, padx=5)
        
        # Botão de remover (para o item selecionado)
        self.btn_remover_selecionado = tk.Button(
            self.frame_acoes, 
            text="Remover Selecionado", 
            command=self.remover_usuario,
            bg='#ff9999',
            width=15
        )
        self.btn_remover_selecionado.pack(side=tk.LEFT, padx=5)
        
        # Adicionando dados de exemplo
        self.adicionar_exemplo("João Silva", "joao@email.com", "123.456.789-00", "2023-05-01")
        self.adicionar_exemplo("Maria Souza", "maria@email.com", "987.654.321-00", "2023-05-02")
        
        # Campos do formulário
        tk.Label(self.frame_formulario, text="Nome:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_formulario, width=40)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_formulario, text="Data de nascimento:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_data_nasc = tk.Entry(self.frame_formulario, width=40)
        self.entry_data_nasc.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_formulario, text="Cpf:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.frame_formulario, width=40)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_formulario, text="Email:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_formulario, width=40)
        self.entry_email.grid(row=3, column=1, padx=5, pady=5)
        
        # Botão de cadastrar no formulário
        self.btn_confirmar = tk.Button(self.frame_formulario, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_confirmar.grid(row=4, column=1, pady=10, sticky="e")

        self.carregar_membros_do_banco()
    
    def carregar_membros_do_banco(self):
        membros = obter_membros()
        for membro in membros:
            # Adiciona os dados na treeview
            self.tree.insert("", "end", values=(
                membro['nome'],
                membro['data_nascimento'],
                membro['cpf'],
                membro['email'],
                membro['data_cadastro']
            ))

    
    def adicionar_exemplo(self, nome, email, cpf, data_cadastro):
        self.tree.insert("", "end", values=(nome, email, cpf, data_cadastro))
    
    def mostrar_formulario(self):
        if not self.formulario_visivel:
            self.frame_formulario.pack(fill=tk.X, padx=10, pady=10)
            self.formulario_visivel = True
        else:
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False
            
    def cadastrar_usuario(self):
        membro = Membro(
            nome = self.entry_nome.get(),
            data_nascimento = self.entry_data_nasc.get(),
            cpf = self.entry_cpf.get(),
            email = self.entry_email.get()
            )        
        if (membro.nome == "" or membro.data_nascimento == "" or membro.cpf == "" or membro.email == ""):
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")

        else:

            criar_membro(membro)
            # Limpar campos após cadastro
            self.entry_nome.delete(0, tk.END)
            self.entry_data_nasc.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
                
            # Esconder o formulário após cadastro
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False

    def remover_usuario(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um registro para remover!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente remover o registro selecionado?")
        if resposta:
            for item in selecionado:
                deletar_membro(item)
                #self.tree.delete(item)
    
    def editar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um registro para editar!")
            return
        
        if len(selecionado) > 1:
            messagebox.showwarning("Aviso", "Selecione apenas um registro para editar!")
            return
        
        item = selecionado[0]
        valores = self.tree.item(item, 'values')
        
        # Mostrar formulário com valores pré-preenchidos
        self.mostrar_formulario()
        
        # Preencher campos
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, valores[0])
        
        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, valores[1])
        
        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, valores[2])
        
        # Atualizar o botão para salvar edição
        self.btn_confirmar.config(text="Salvar Edição", command=lambda: self.salvar_edicao(item))

    def salvar_edicao(self, item):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        data_nasc = self.entry_data_nasc.get()
        
        if nome and cpf and email:
            # Atualizar os valores na treeview
            self.tree.item(item, values=(nome, email, cpf, data_nasc))
            
            # Limpar campos
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_data_nasc.delete(0, tk.END)
            
            # Esconder o formulário
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False
            
            # Restaurar o botão para cadastrar
            self.btn_confirmar.config(text="Cadastrar", command=self.cadastrar_usuario)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")