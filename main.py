from tkinter import *
from db import Database
from tkinter import messagebox

def chamacliente():
    from cadastrocliente import TelaCadastro
    janela.destroy()
    TelaCadastro()

def chamapres():
    from loginPres import LoginProfissional
    janela.destroy()
    LoginProfissional()

def vizualizaPres():
    from exibepres import Vizualiza
    usuario = caixaUser.get()
    senha = caixaSenha.get()
    user_id = db.verificaLogin(usuario, senha)
    
    if user_id:
        janela.destroy()
        Vizualiza(user_id)  # Passar o ID para a próxima tela
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

db = Database(r"C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\clientes.db")

janela = Tk()
fonte = ("LASTICA", 8)
labelcor = Label(bg='gray', width=120, height=100)
labelcor.pack(side=LEFT)
labelcor2 = Label(bg='#D3D3D3', width=80, height=70)
labelcor2.pack()

# LOGO
titulo = Label(text="S-SOLUTION", font=("Comic Sans MS", 30, "bold"), bg='black', fg='orange')
titulo.place(x=550, y=100)
titulo.config(relief='ridge', bd=7,)

# LOGIN
labelogin = Label(text='Login', font=('Courier New', 60), bg='#D3D3D3')
labelogin.place(x=950, y=100)
labelUser = Label(text='Usuario', font=('Courier New', 12), bg='#D3D3D3')
labelUser.place(x=950, y=200)
caixaUser = Entry(width=15)
caixaUser.place(x=1029, y=200)
caixaUser.config(relief='flat')
labelSenha = Label(text='Senha', font=('Courier New', 12), bg='#D3D3D3')
labelSenha.place(x=950, y=220)
caixaSenha = Entry(width=18)
caixaSenha.place(x=1010, y=220)
caixaSenha.config(relief='flat', show='*', bd=1)

# BOTOES
Entrar = Button(text="Entrar", font=('Courier New', 14), bg='#D3D3D3', command=vizualizaPres)
Entrar.place(x=1000, y=250)
Entrar.config(relief='groove')
cadastro = Button(text='Cadastre-se', font=('Courier New', 8), bg='#D3D3D3', command=chamacliente)
cadastro.place(x=1000, y=290)
cadastro.config(relief='groove')
labelpres = Label(text='Perfil Profissional', font=('Courier New', 20), bg='#D3D3D3')
labelpres.place(x=900, y=550)
centralprestador = Button(text='->', font=('Courier New', 15), bg='#D3D3D3', command=chamapres)
centralprestador.config(relief='groove')
centralprestador.place(x=1220, y=550)

mainloop()
