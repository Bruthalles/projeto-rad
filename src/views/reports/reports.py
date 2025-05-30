import tkinter as tk
from controllers.logs import relatorio_operacoes

def Pg_Reports():
    root = tk.Toplevel()
    root.title("Relatório de operações")
    
    largura_janela = 900
    altura_janela = 500

    largura_tela = root.winfo_screenwidth()
    altura_Tela = root.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_Tela // 2) - (altura_janela // 2)
    root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

    aviso = tk.Label(root,text='Relatório completo encontra-se no arquivo relatorio_operacoes.txt',font=("Arial",16,'bold'))
    aviso.pack()
    text_area = tk.Text(root,wrap=tk.WORD)
    text_area.pack(expand=True,fill=tk.BOTH)

    for linha in relatorio_operacoes:
        text_area.insert(tk.END, linha + '\n')

    root.mainloop()