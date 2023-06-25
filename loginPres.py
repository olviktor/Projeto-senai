from tkinter import *
from db import Prestadores
from tkinter import messagebox

class LoginProfissional:
    def __init__(self):
        self.db = Prestadores(r"C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\prestadores.db")

        self.janela9 = Tk()
        self.fonte = ("LASTICA", 8)
        self.labelcor = Label(bg='white', width=120, height=100)
        self.labelcor.pack(side=LEFT)
        self.labelcor2 = Label(bg='#D3D3D3', width=80, height=70)
        self.labelcor2.pack()

        # LOGO
        self.titulo = Label(text="S-SOLUTION", font=("Comic Sans MS", 30, "bold"), bg='black', fg='orange')
        self.titulo.place(x=553, y=100)
        self.titulo.config(relief='ridge', bd=7)

        # LOGIN
        self.labelogin = Label(text='Login\nProfissional', font=('Courier New', 40), bg='#D3D3D3')
        self.labelogin.place(x=900, y=50)
        self.labelUser = Label(text='Usuario', font=('Courier New', 12), bg='#D3D3D3')
        self.labelUser.place(x=950, y=200)
        self.caixaUser = Entry(width=15)
        self.caixaUser.place(x=1029, y=200)
        self.caixaUser.config(relief='flat')
        self.labelSenha = Label(text='Senha', font=('Courier New', 12), bg='#D3D3D3')
        self.labelSenha.place(x=950, y=220)
        self.caixaSenha = Entry(width=18)
        self.caixaSenha.place(x=1010, y=220)
        self.caixaSenha.config(relief='flat', show='*', bd=1)

        # BOTOES
        self.entrar_button = Button(text="Entrar", font=('Courier New', 14), bg='#D3D3D3', command=self.vizualizaclientes)
        self.entrar_button.place(x=1000, y=250)
        self.entrar_button.config(relief='groove')
        self.cadastro_button = Button(text='Cadastre-se', font=('Courier New', 8), bg='#D3D3D3', command=self.chamacadastro)
        self.cadastro_button.place(x=1000, y=290)
        self.cadastro_button.config(relief='groove')

        self.janela9.mainloop()

    def chamacadastro(self):
        from cadastropres import CadastroPres
        self.janela9.destroy()
        CadastroPres()

    def vizualizaclientes(self):
        usuario = self.caixaUser.get()
        senha = self.caixaSenha.get()
        user_id = self.db.verificaLogin(usuario, senha)

        if user_id:
            self.janela9.destroy()
            from exibeclientes import Vizualizacliente
            Vizualizacliente(user_id)  # Passar o ID para a próxima tela
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
