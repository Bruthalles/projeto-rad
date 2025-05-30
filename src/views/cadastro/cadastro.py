import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from models.Membro import Membro
from models.db import BancoDeDados
from controllers.create_membro import criar_membro
from controllers.read_membro import obter_membros
from controllers.update_membro import atualizar_membro
from controllers.delete_membro import deletar_membro
from views.reports.reports import Pg_Reports

def Pg_Cadastro():
    root = tk.Tk()
    banco = BancoDeDados()
    banco.conectar_banco()
    banco.criar_tabela()
    app = CadastroApp(root)
    root.mainloop()

class CadastroApp:

    def reload(self):
        self.root.destroy()
        Pg_Cadastro()

    def change_page(self):
        self.root.destroy()
        from views.home.home import Pg_Home #evita import circular
        Pg_Home()

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        
        largura_janela = 900
        altura_janela = 700

        largura_tela = root.winfo_screenwidth()
        altura_Tela = root.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_Tela // 2) - (altura_janela // 2)
        root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')


        # Variável para controlar se o formulário está visível
        self.formulario_visivel = False
        
        # Frame do formulário de cadastro (inicialmente oculto)
        self.frame_formulario = tk.Frame(root)

        # Frame superior com botões
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=10,fill='x')

        #Frames divisor de botoes
        self.frame_btn_left = tk.Frame(self.frame_botoes)
        self.frame_btn_left.pack(side=tk.LEFT,anchor='w',padx=(7,0))

        self.frame_btn_right = tk.Frame(self.frame_botoes)
        self.frame_btn_right.pack(padx=(0,7),side=tk.RIGHT,anchor='e')
        
        #Icones
        img_load = Image.open('src/icons/reload.png')
        load_resize = img_load.resize((24,24))
        self.icn_load = ImageTk.PhotoImage(load_resize)

        img_back = Image.open('src/icons/back.png')
        back_resize = img_back.resize((24,24))
        self.icn_back = ImageTk.PhotoImage(back_resize)
        
        #Botoes
        self.btn_back = tk.Button(self.frame_btn_left, image=self.icn_back,command=self.change_page)
        self.btn_back.pack(side=tk.LEFT, padx=(5,10))

        self.btn_reload = tk.Button(self.frame_btn_left,image=self.icn_load,command=self.reload)
        self.btn_reload.pack(side=tk.LEFT)
        
        self.btn_cadastrar = tk.Button(self.frame_btn_right, text="Cadastrar", command=self.mostrar_formulario)
        self.btn_cadastrar.pack(side=tk.LEFT, padx=(0,10))

        self.btn_editar = tk.Button(self.frame_btn_right, text="Editar", command=self.carregar_membro_para_edicao)
        self.btn_editar.pack(side=tk.LEFT, padx=5)

        self.btn_remover = tk.Button(self.frame_btn_right, text="Remover", command=self.remover_membro)
        self.btn_remover.pack(side=tk.LEFT, padx=5)
        
        self.btn_reports = tk.Button(self.frame_btn_right, text="Relatórios",command=Pg_Reports)
        self.btn_reports.pack(side=tk.LEFT, padx=(0,5))
        
        # Frame da lista de registros
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=1)
        
        # Scrollbar
        scrollbar_x = ttk.Scrollbar(self.frame_lista, orient='vertical')

        # Treeview para exibir os registros
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID","Nome","Data de Nascimento", "CPF", "Email", "Data Cadastro","Status"), show="headings",yscrollcommand=scrollbar_x.set)

        # Configurando Scroll
        scrollbar_x.config(command=self.tree.yview)
        scrollbar_x.pack(side='left',fill='y')
        
        # Configurar cabeçalhos
        self.tree.heading("ID",text='ID')
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Data de Nascimento",text="Data de Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Data Cadastro", text="Data Cadastro")
        self.tree.heading("Status",text="Status")
        
        # Configurar colunas
        self.tree.column("ID",width=50)
        self.tree.column("Nome", width=170)
        self.tree.column("Data de Nascimento", width=100)
        self.tree.column("CPF", width=100)
        self.tree.column("Email", width=170)
        self.tree.column("Data Cadastro", width=90)
        self.tree.column("Status",width=55)

        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Frame para botões de ação (alternativa à coluna Ações)
        self.frame_acoes = tk.Frame(root)
        self.frame_acoes.pack(pady=5)
        
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
        self.btn_confirmar = tk.Button(self.frame_formulario, text="Cadastrar", command=self.cadastrar_membro)
        self.btn_confirmar.grid(row=4, column=1, pady=10, sticky="e")

        self.carregar_membros_do_banco()
    
    def carregar_membros_do_banco(self):
        membros = obter_membros()
        for membro in membros:
            # Adiciona os dados na treeview
            self.tree.insert("", "end", iid=membro['id'] ,values=(
                membro['id'],
                membro['nome'],
                membro['data_nascimento'],
                membro['cpf'],
                membro['email'],
                membro['data_cadastro'],
                membro['status']
            ))

    def mostrar_formulario(self):
        if not self.formulario_visivel:
            self.frame_formulario.pack(fill=tk.X, padx=10, pady=10)
            self.formulario_visivel = True
        else:
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False
            
    def cadastrar_membro(self):
        membro = Membro(
        nome=self.entry_nome.get(),
        data_nascimento=self.entry_data_nasc.get(),
        cpf=self.entry_cpf.get(),
        email=self.entry_email.get()
        )
        
        if not all([membro.nome, membro.data_nascimento, membro.cpf, membro.email]):
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")
            return

        # Se estiver editando um membro
        if hasattr(self, 'id_membro_edicao'):
            novos_dados = {
                'nome': membro.nome,
                'data_nascimento': membro.data_nascimento,
                'cpf': membro.cpf,
                'email': membro.email
            }
            atualizar_membro(self.id_membro_edicao, novos_dados)
            messagebox.showinfo("Sucesso", "Membro atualizado com sucesso!")
            del self.id_membro_edicao  # Limpa o modo de edição
        else:
            if criar_membro(membro):
                messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
            else:
                messagebox.showerror("Erro", "Já existe um membro com este CPF!")
                return

        # Limpar e atualizar
        self.entry_nome.delete(0, tk.END)
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.frame_formulario.pack_forget()
        self.formulario_visivel = False
        self.atualizar_treeview()

    def atualizar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.carregar_membros_do_banco()

    def remover_membro(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um registro para remover!")
            return
        
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente remover o registro selecionado?")
        if resposta:
            
            for item in selecionado:

                item_id = self.tree.item(selecionado[0])
                valores = item_id['values']
                id = valores[0]
                cpf = valores[3]
                
                resultado = deletar_membro(id,cpf)
                if resultado > 0:
                    self.tree.delete(item)
                    messagebox.showinfo("Sucesso","Membro Removido")
                else:
                    messagebox.showerror("Erro","Não foi possível remover membro")
    
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

    def carregar_membro_para_edicao(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso","Selecione um membro para editar")
            return
        
        membro_id = selecionado[0]
        valores = self.tree.item(membro_id,'values')

        #Preencher campos com os dados
        self.entry_nome.delete(0,tk.END)
        self.entry_nome.insert(0,valores[1])

        self.entry_data_nasc.delete(0, tk.END)
        self.entry_data_nasc.insert(0, valores[2])

        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, valores[3])

        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, valores[4])

        #guardando id para função salvar
        self.id_membro_edicao = membro_id
        self.frame_formulario.pack()
        self.formulario_visivel = True

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
            self.btn_confirmar.config(text="Cadastrar", command=self.cadastrar_membro)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")