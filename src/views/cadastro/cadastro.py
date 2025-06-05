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
import re
from datetime import datetime

#Cores personalizadas
COR_FUNDO = "#a7bdda"
COR_PRIMARIA = "#4f64aa"
COR_BTN_TEXTO = "#ffffffee"

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
        self.root.configure(bg=COR_FUNDO)
        
        largura_janela = 1100
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
        self.frame_botoes.configure(bg=COR_FUNDO)

        #Frames divisor de botoes
        self.frame_btn_left = tk.Frame(self.frame_botoes)
        self.frame_btn_left.pack(side=tk.LEFT,anchor='w',padx=(7,0))
        self.frame_btn_left.configure(bg=COR_FUNDO)

        self.frame_btn_right = tk.Frame(self.frame_botoes)
        self.frame_btn_right.pack(padx=(0,7),side=tk.RIGHT,anchor='e')
        self.frame_btn_right.configure(bg=COR_FUNDO)
        
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
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID","Nome","Data de Nascimento", "CPF", "Email","Atestado", "Data Cadastro"), show="headings",yscrollcommand=scrollbar_x.set)

        # Configurando Scroll
        scrollbar_x.config(command=self.tree.yview)
        scrollbar_x.pack(side='left',fill='y')
        
        # Configurar cabeçalhos
        self.tree.heading("ID",text='ID')
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Data de Nascimento",text="Data de Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Atestado",text="Atestado")
        self.tree.heading("Data Cadastro", text="Data Cadastro")
        
        
        # Configurar colunas
        self.tree.column("ID",width=50)
        self.tree.column("Nome", width=170)
        self.tree.column("Data de Nascimento", width=100)
        self.tree.column("CPF", width=100)
        self.tree.column("Email", width=170)
        self.tree.column("Atestado",width=100)
        self.tree.column("Data Cadastro", width=90)

        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Frame para botões de ação (alternativa à coluna Ações)
        self.frame_acoes = tk.Frame(root)
        self.frame_acoes.pack(pady=5)
        
        # Campos do formulário
        tk.Label(self.frame_formulario, text="Nome:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_formulario, width=40)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nome.bind("<KeyRelease>", self.validar_nome_em_tempo_real)
        
        tk.Label(self.frame_formulario, text="Data de nascimento:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_data_nasc = tk.Entry(self.frame_formulario, width=40)
        self.entry_data_nasc.grid(row=1, column=1, padx=5, pady=5)
        self.entry_data_nasc.bind("<KeyRelease>", self.formatar_data_nascimento)
        
        tk.Label(self.frame_formulario, text="CPF:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.frame_formulario, width=40)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)
        self.entry_cpf.bind("<KeyRelease>", self.formatar_cpf)
        
        tk.Label(self.frame_formulario, text="Email:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_formulario, width=40)
        self.entry_email.grid(row=3, column=1, padx=5, pady=5)
        self.entry_email.bind("<FocusOut>", self.validar_email_em_tempo_real)

        tk.Label(self.frame_formulario,text="Número do atestado:").grid(row=4,column=0,sticky="e",padx=5,pady=5)
        self.entry_atestado = tk.Entry(self.frame_formulario,width=40)
        self.entry_atestado.grid(row=4, column=1, padx=5, pady=5)
        self.entry_atestado.bind("<FocusOut>", self.validar_atestado_em_tempo_real)
        
        # Botão de cadastrar no formulário
        self.btn_enviar = tk.Button(self.frame_formulario, text="Cadastrar", command=self.cadastrar_membro)
        self.btn_enviar.grid(row=4, column=1, pady=10, sticky="e")

        # Labels para feedback de validação
        self.lbl_feedback_nome = tk.Label(self.frame_formulario, text="", fg="red")
        self.lbl_feedback_nome.grid(row=0, column=2, padx=5)
        
        self.lbl_feedback_data = tk.Label(self.frame_formulario, text="", fg="red")
        self.lbl_feedback_data.grid(row=1, column=2, padx=5)
        
        self.lbl_feedback_cpf = tk.Label(self.frame_formulario, text="", fg="red")
        self.lbl_feedback_cpf.grid(row=2, column=2, padx=5)
        
        self.lbl_feedback_email = tk.Label(self.frame_formulario, text="", fg="red")
        self.lbl_feedback_email.grid(row=3, column=2, padx=5)

        self.lbl_feedback_atestado = tk.Label(self.frame_formulario, text="",fg="red")
        self.lbl_feedback_atestado.grid(row=4,column=2,padx=5)

        self.carregar_membros_do_banco()
    
    # Métodos de validação
    def validar_nome(self, nome):
        """Valida se o nome tem até 20 caracteres e apenas letras e espaços"""
        return bool(re.match(r'^[a-zA-ZÀ-ÿ\s]{1,20}$', nome.strip()))

    def validar_data_nascimento(self, data_str):
        """Valida se a data é numérica e converte para formato date"""
        try:
            # Verifica se tem apenas números e formato básico de data
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_str.strip()):
                return None
            
            # Converte para objeto date
            return datetime.strptime(data_str.strip(), '%d/%m/%Y').date()
        except ValueError:
            return None

    def validar_cpf(self, cpf):
        """Valida se o CPF tem 11 dígitos numéricos"""
        cpf_limpo = re.sub(r'[^\d]', '', cpf)  # Remove não-dígitos
        return len(cpf_limpo) == 11

    def validar_email(self, email):
        """Valida o formato básico de email"""
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email.strip()))        

    # Métodos de formatação e validação em tempo real
    def validar_nome_em_tempo_real(self, event):
        nome = self.entry_nome.get()
        if not self.validar_nome(nome):
            self.lbl_feedback_nome.config(text="Máx 20 caracteres, apenas letras")
        else:
            self.lbl_feedback_nome.config(text="")

    def formatar_data_nascimento(self, event):
        data = self.entry_data_nasc.get()
        data_limpa = re.sub(r'[^\d]', '', data)
        
        if len(data_limpa) > 8:
            data_limpa = data_limpa[:8]
        
        data_formatada = ""
        for i in range(len(data_limpa)):
            if i == 2 or i == 4:
                data_formatada += "/"
            data_formatada += data_limpa[i]
        
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_data_nasc.insert(0, data_formatada)
        
        # Validação
        if not self.validar_data_nascimento(data_formatada):
            self.lbl_feedback_data.config(text="Formato DD/MM/AAAA")
        else:
            self.lbl_feedback_data.config(text="")

    def formatar_cpf(self, event):
        cpf = self.entry_cpf.get()
        cpf_limpo = re.sub(r'[^\d]', '', cpf)
        
        if len(cpf_limpo) > 11:
            cpf_limpo = cpf_limpo[:11]
        
        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, cpf_limpo)
        
        # Validação
        if not self.validar_cpf(cpf_limpo):
            self.lbl_feedback_cpf.config(text="11 dígitos necessários")
        else:
            self.lbl_feedback_cpf.config(text="")

    def validar_email_em_tempo_real(self, event):
        email = self.entry_email.get()
        if not self.validar_email(email):
            self.lbl_feedback_email.config(text="Email inválido")
        else:
            self.lbl_feedback_email.config(text="")
    
    def validar_atestado(self, valor):
        """Valida se o atestado contém somente números e 6 a 12 dígitos"""
        return bool(re.match(r'^\d{6,12}$', valor.strip()))

    def validar_atestado_em_tempo_real(self, event):
        valor = self.entry_atestado.get()
        if not self.validar_atestado(valor):
            self.lbl_feedback_atestado.config(text="Atestado deve ter 6 a 12 números")
        else:
            self.lbl_feedback_atestado.config(text="")


    # Métodos existentes com as novas validações
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
                membro['atestado'],
                membro['data_cadastro']
            
            ))

    def mostrar_formulario(self):
        if not self.formulario_visivel:
            self.frame_formulario.pack(fill=tk.X, padx=10, pady=10)
            self.formulario_visivel = True
            # Limpar feedbacks ao mostrar o formulário
            self.lbl_feedback_nome.config(text="")
            self.lbl_feedback_data.config(text="")
            self.lbl_feedback_cpf.config(text="")
            self.lbl_feedback_email.config(text="")
        else:
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False
            
    def cadastrar_membro(self):
        # Obter valores dos campos
        nome = self.entry_nome.get().strip()
        data_nasc_str = self.entry_data_nasc.get().strip()
        cpf = self.entry_cpf.get().strip()
        email = self.entry_email.get().strip()
        atestado = self.entry_atestado.get().strip()

        # Validações
        if not self.validar_nome(nome):
            messagebox.showwarning("Aviso", "Nome inválido! Máximo 20 caracteres e apenas letras.")
            return

        data_nasc = self.validar_data_nascimento(data_nasc_str)
        if not data_nasc:
            messagebox.showwarning("Aviso", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
            return

        if not self.validar_cpf(cpf):
            messagebox.showwarning("Aviso", "CPF inválido! Deve conter 11 dígitos.")
            return

        if not self.validar_email(email):
            messagebox.showwarning("Aviso", "Email inválido! Deve conter @ e domínio válido.")
            return
        
        if not self.validar_atestado(atestado):
            messagebox.showwarning("Aviso","Complete o campo atestado.")
            return
        

        # Formatar CPF (remove caracteres não numéricos)
        cpf_formatado = re.sub(r'[^\d]', '', cpf)

        # Criar objeto Membro com dados validados
        membro = Membro(
            nome=nome,
            data_nascimento=data_nasc.strftime('%Y-%m-%d'),  # Formato SQL
            cpf=cpf_formatado,
            email=email,
            atestado=atestado
        )

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
        self.entry_nome.insert(0, valores[1])
        
        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, valores[4])
        
        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, valores[3])
        
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_data_nasc.insert(0, valores[2])
        
        # Atualizar o botão para salvar edição
        self.btn_enviar.config(text="Salvar Edição", command=lambda: self.salvar_edicao(item))

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

    def cadastrar_membro(self):
        nome = self.entry_nome.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()
        cpf = self.entry_cpf.get().strip()
        email = self.entry_email.get().strip()
        atestado = self.entry_atestado.get().strip()

        # Validações
        erros = []

        if not self.validar_nome(nome):
            erros.append("Nome inválido")

        data_convertida = self.validar_data_nascimento(data_nasc)
        if not data_convertida:
            erros.append("Data de nascimento inválida")

        if not self.validar_cpf(cpf):
            erros.append("CPF inválido")

        if not self.validar_email(email):
            erros.append("Email inválido")

        if not self.validar_atestado(atestado):
            erros.append("Número do atestado inválido")

        if erros:
            messagebox.showerror("Erro de validação", "\n".join(erros))
            return

        # Cria e salva no banco
        membro = Membro(nome, str(data_convertida), cpf, email, atestado)
        sucesso = criar_membro(membro)

        if sucesso:
            messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso.")
            self.frame_formulario.pack_forget()
            self.formulario_visivel = False
            self.carregar_membros_do_banco()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar membro.")


    def salvar_edicao(self, item):
        # Obter valores validados
        nome = self.entry_nome.get().strip()
        data_nasc_str = self.entry_data_nasc.get().strip()
        cpf = self.entry_cpf.get().strip()
        email = self.entry_email.get().strip()

        # Validações
        if not self.validar_nome(nome):
            messagebox.showwarning("Aviso", "Nome inválido! Máximo 20 caracteres e apenas letras.")
            return

        data_nasc = self.validar_data_nascimento(data_nasc_str)
        if not data_nasc:
            messagebox.showwarning("Aviso", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
            return

        if not self.validar_cpf(cpf):
            messagebox.showwarning("Aviso", "CPF inválido! Deve conter 11 dígitos.")
            return

        if not self.validar_email(email):
            messagebox.showwarning("Aviso", "Email inválido! Deve conter @ e domínio válido.")
            return

        # Atualizar os valores na treeview
        self.tree.item(item, values=(
            self.tree.item(item, 'values')[0],  # Mantém o ID
            nome,
            data_nasc_str,
            cpf,
            email,
            self.tree.item(item, 'values')[5],  # Mantém a data de cadastro
            self.tree.item(item, 'values')[6]   # Mantém o status
        ))
        
        # Limpar campos
        self.entry_nome.delete(0, tk.END)
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        
        # Esconder o formulário
        self.frame_formulario.pack_forget()
        self.formulario_visivel = False
        
        # Restaurar o botão para cadastrar
        self.btn_enviar.config(text="Cadastrar", command=self.cadastrar_membro)