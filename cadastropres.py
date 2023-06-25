from tkinter import *
from db import Prestadores
from tkinter import ttk
from tkinter import messagebox
class CadastroPres:
    def __init__(self):
        self.db = Prestadores(r"C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\prestadores.db")
        self.janela3 = Tk()
        self.fonte = ('Courier New', 12, 'bold')
        self.labelcor = Label(width=200, height=200, bg='#FF8C00')
        self.labelcor.pack()
        self.titulo = Label(text='CADASTRO PROFISSIONAL', font=('Courier New', 20, 'bold'), bg='#FF8C00')
        self.titulo.place(x=0, y=0)
        self.labelnome = Label(text='Nome', font=self.fonte, bg='#FF8C00')
        self.labelnome.place(x=50, y=200)
        self.labelnome.config(relief='flat')
        self.labelTelefone = Label(text='Telefone', font=self.fonte, bg='#FF8C00')
        self.labelTelefone.place(x=50, y=250)
        self.labelcpf = Label(text='CPF', font=self.fonte, bg='#FF8C00')
        self.labelcpf.place(x=50, y=300)
        self.labelemail = Label(text='Email', font=self.fonte, bg='#FF8C00')
        self.labelemail.place(x=50, y=350)
        self.labelusuario = Label(text='Usuario', font=self.fonte, bg='#FF8C00')
        self.labelusuario.place(x=50, y=400)
        self.labelsenha = Label(text='Senha', font=self.fonte, bg='#FF8C00')
        self.labelsenha.place(x=50, y=450)
        self.genero1 = Label(text='Genero', font=self.fonte, bg='#FF8C00')
        self.genero1.place(x=50, y=500)
        self.endereco = Label(text='Endereço', font=self.fonte, bg='#FF8C00')
        self.endereco.place(x=720, y=180)
        self.num = Label(text='Numero', font=self.fonte, bg='#FF8C00')
        self.num.place(x=720, y=240)
        self.profissao = Label(text='Profisão', font=self.fonte, bg='#FF8C00')
        self.profissao.place(x=720, y=300)

        self.caixanome = Entry(width=50)
        self.caixanome.place(x=150, y=200)
        self.caixanome.config(relief='solid', bd=1)
        self.caixatelefone = Entry(width=50)
        self.caixatelefone.place(x=150, y=250)
        self.caixatelefone.config(relief='solid', bd=1)
        self.caixacpf = Entry(width=50)
        self.caixacpf.place(x=150, y=300)
        self.caixacpf.config(relief='solid', bd=1)
        self.caixaemail = Entry(width=47)
        self.caixaemail.place(x=150, y=350)
        self.caixaemail.config(relief='solid', bd=1)
        self.caixausuario = Entry(width=30)
        self.caixausuario.place(x=150, y=400)
        self.caixausuario.config(relief='solid', bd=1)
        self.caixasenha = Entry(width=30)
        self.caixasenha.place(x=150, y=450)
        self.caixasenha.config(relief='solid', bd=1, show='*')
        self.caixanum = Entry(width=3)
        self.caixanum.place(x=790, y=240)
        self.comboGenero = ttk.Combobox(font=self.fonte, state='readonly', width=10)
        self.comboGenero['values'] = ("Masculino", 'Feminino', "Outro")
        self.comboGenero.place(x=150, y=500)
        self.enderecos = Text(width=40, height=1)
        self.enderecos.place(x=720, y=200)
        self.comboestado = ttk.Combobox(font=self.fonte, state='readonly', width=2)
        self.comboestado['values'] = ('BA', 'SE', 'CE')
        self.comboestado.place(x=1050, y=200)
        self.comboprofissao = ttk.Combobox(font=self.fonte, state='readonly', width=6)
        self.comboprofissao['values'] = ('Pedreiro', 'Pintor', 'Carpinteiro')
        self.comboprofissao.place(x=820, y=300)
        self.botaosalva = Button(text='Salvar e Entrar', font=self.fonte, command=lambda:self.salvaPres_e_entrar())
        self.botaosalva.place(x=920, y=500)
        self.botaosalva.config(relief='ridge', border=4, bd=2)


        mainloop()

    def salvaPres_e_entrar(self):
        nome = self.caixanome.get()
        telefone = self.caixatelefone.get()
        cpf = self.caixacpf.get()
        email = self.caixaemail.get()
        usuario = self.caixausuario.get()
        senha = self.caixasenha.get()
        genero = self.comboGenero.get()
        endereco = self.enderecos.get(1.0, END)
        estado = self.comboestado.get()
        profissao = self.comboprofissao.get()
       

        if nome and telefone and cpf and email and usuario and senha and genero and endereco and estado and profissao:
              
              self.db.insertpres(nome, telefone, cpf, email, usuario, senha, genero, endereco, estado, profissao)
              user_id=self.db.get_last_inserted_idpres()
              messagebox.showinfo("Tudo certo",'Cadastro realizado com sucesso')
              self.entrar(user_id)
              print("valor do novo id cadastrado {}".format(user_id))
             
        else:
             messagebox.showinfo("Algo deu errado",'Preencha todos os campos')
    def entrar(self,user_id):
        from exibeclientes import Vizualizacliente
        self.janela3.destroy()
        Vizualizacliente(user_id)


