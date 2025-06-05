import tkinter as tk
from tkinter import PhotoImage
from controllers.read_membro import obter_membros
from views.cadastro.cadastro import Pg_Cadastro
from views.reports.reports import Pg_Reports

font_size = 14

def Pg_Home():
    root = tk.Tk()
    root.title("Membros cadastrados")

    largura_janela = 525
    altura_janela = 700

    largura_tela = root.winfo_screenwidth()
    altura_Tela = root.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_Tela // 2) - (altura_janela // 2)
    root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

    def change_page():
        root.destroy()
        Pg_Cadastro()

    # Seção para botões
    frame_botoes = tk.Frame(root)
    frame_botoes.pack(padx=10, pady=10)

    lb = tk.Label(root, text='Lista de membros', font=("Arial", 15))
    lb.pack()

    # Scrollbar
    container = tk.Frame(root)
    container.pack(fill='both', expand=True)

    canvas = tk.Canvas(container, bg='white')
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side='right', fill='y')
    canvas.pack(side='left', fill='both', expand=True)

    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Botão para cadastro
    dados = tk.Button(frame_botoes, text='Base de Dados', command=change_page)
    dados.pack(padx=(5, 12), pady=(5, 12))

    # Ícone de usuário
    user_icon = PhotoImage(file="src/icons/user_icon.png")  # Ajuste o caminho conforme necessário

    # Seção de membros
    section_membro = tk.Frame(scrollable_frame, padx=10, pady=10)
    section_membro.pack(fill='both', expand=True)

    # Frame interno que centraliza os cards horizontalmente
    container_cards = tk.Frame(section_membro)
    container_cards.pack(anchor='center')

    for membro in obter_membros():
        card = tk.Frame(container_cards, bd=2, relief='groove', bg='lightblue', padx=10, pady=10, width=480, height=230)
        card.pack(anchor='center', padx=10, pady=10)
        card.pack_propagate(False)

        # Frame lateral direito com imagem e status empilhados verticalmente
        img_status_frame = tk.Frame(card, bg='lightblue')
        img_status_frame.pack(side='right', padx=10, pady=5)

        img_label = tk.Label(img_status_frame, image=user_icon, bg='lightblue')
        img_label.pack()

        status_label = tk.Label(img_status_frame, text=f'{membro["atestado"]}', font=("Arial", font_size), bg='lightblue')
        status_label.pack(pady=(10, 0))

        # Frame com informações lado a lado em colunas
        info_frame = tk.Frame(card, bg='lightblue')
        info_frame.pack(side='left', padx=10, pady=5, fill='y')

        # Labels com título em cima e valor embaixo
        dados_membro = [
            ("ID", membro["id"]),
            ("Nome", membro["nome"].capitalize()),
            ("Nascimento", membro["data_nascimento"]),
            ("CPF", membro["cpf"]),
            ("E-mail", membro["email"]),
            ("Cadastro", membro["data_cadastro"]),
        ]

        # Layout: duas colunas (0 e 1) com título e valor um abaixo do outro
        for i in range(0, len(dados_membro) - 1, 2):
            # Coluna 1
            tk.Label(info_frame, text=dados_membro[i][0], font=("Arial", font_size, 'bold'), bg='lightblue').grid(row=i, column=0, sticky='w')
            tk.Label(info_frame, text=dados_membro[i][1], font=("Arial", font_size), bg='lightblue').grid(row=i+1, column=0, sticky='w', padx=(5, 20), pady=(0, 10))

            # Coluna 2 (se existir)
            if i + 1 < len(dados_membro):
                tk.Label(info_frame, text=dados_membro[i+1][0], font=("Arial", font_size, 'bold'), bg='lightblue').grid(row=i, column=1, sticky='w')
                tk.Label(info_frame, text=dados_membro[i+1][1], font=("Arial", font_size), bg='lightblue').grid(row=i+1, column=1, sticky='w', pady=(0, 10))

    root.mainloop()
