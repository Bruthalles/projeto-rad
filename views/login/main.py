from tkinter import * 

pg_login = Tk()
pg_login.title("Emissão de Carteirinhas - Login")
pg_login.resizable(False,False)
txt_login = Label(pg_login,text="Login")
txt_login.grid(column=0,row=0)

txt_usr = Label(pg_login,text='Usuário')
txt_usr.grid(column=0,row=1)




pg_login.mainloop()
