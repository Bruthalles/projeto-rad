import tkinter as tk
from controllers.logs import relatorio_operacoes

def Pg_Reports():
    root = tk.Toplevel()
    root.title("Relatório de operações")
    root.geometry('900x500')

    aviso = tk.Label(root,text='Relatório completo encontra-se no arquivo relatorio_operacoes.txt',font=("Arial",16,'bold'))
    aviso.pack()
    text_area = tk.Text(root,wrap=tk.WORD)
    text_area.pack(expand=True,fill=tk.BOTH)

    for linha in relatorio_operacoes:
        text_area.insert(tk.END, linha + '\n')

    root.mainloop()