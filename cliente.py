from tkinter import*
from tkinter import ttk
from db import Database
from tkinter import messagebox
from turtle import bgcolor, heading
from tela3 import View

class TelaCadastro:
    def __init__(self):
        self.db=Database(r"C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\clientes.db")
        self.janela2=Tk()
        #janela confings
        self.fonte=('Courier New',12,)
        self.labelcor=Label(width=200,height=200)
        self.labelcor.pack()
        #textos
        self.titulo=Label(text='DADOS CADASTRAIS',font=('Courier New',30))
        self.titulo.place(x=500,y=100)

#LABEL INFOS
        self.labelnome=Label(text='Nome',font=self.fonte)
        self.labelnome.place(x=50,y=200)
        self.labelnome.config(relief='flat')
        self.labelTelefone=Label(text='Telefone',font=self.fonte)
        self.labelTelefone.place(x=50,y=250)
        self.labelcpf=Label(text='CPF',font=self.fonte)
        self.labelcpf.place(x=50,y=300)
        self.labelemail=Label(text='Email',font=self.fonte)
        self.labelemail.place(x=50,y=350)
        self.labelusuario=Label(text='Usuario',font=self.fonte)
        self.labelusuario.place(x=50,y=400)
        self.labelsenha=Label(text='Senha',font=self.fonte)
        self.labelsenha.place(x=50,y=450)
        self.genero1=Label(text='Genero')
        self.genero1.place(x=50,y=500)
        self.endereco=Label(text='Endereço',font=('Courier New',12))
        self.endereco.place(x=720,y=180)
        self.num=Label(text='Numero',font=('Courier New',12))
        self.num.place(x=720,y=240)
        
        
#CAIXAS INFOS
        self.caixanome=Entry(width=50)
        self.caixanome.place(x=150,y=200)
        self.caixanome.config(relief='solid',bd=1)
        self.caixatelefone=Entry(width=50)
        self.caixatelefone.place(x=150,y=250)
        self.caixatelefone.config(relief='solid',bd=1)
        self.caixacpf=Entry(width=50)
        self.caixacpf.place(x=150,y=300)
        self.caixacpf.config(relief='solid',bd=1)
        self.caixaemail=Entry(width=47)
        self.caixaemail.place(x=150,y=350)
        self.caixaemail.config(relief='solid',bd=1)
        self.caixausuario=Entry(width=30)
        self.caixausuario.place(x=150,y=400)
        self.caixausuario.config(relief='solid',bd=1)
        self.caixasenha=Entry(width=30)
        self.caixasenha.place(x=150,y=450)
        self.caixasenha.config(relief='solid',bd=1,show='*')
        self.caixanum=Entry(width=3)
        self.caixanum.place(x=790,y=240)    
        self.comboGenero= ttk.Combobox(font=self.fonte,state='readonly',width=10)
        self.comboGenero['values']=("Masculino",'Feminino',"Outro",)
        self.comboGenero.place(x=150,y=500)
        self.enderecos=Text(width=40,height=1)
        self.enderecos.place(x=720,y=200)
        self.comboestado=ttk.Combobox(font=self.fonte,state='readonly',width=2)
        self.comboestado['values']=('BA','SE','CE')
        self.comboestado.place(x=1050,y=200)
        self.labelmensage=Label(text=['text'])
        

#BOTOES
        self.botaosalva=Button(text='Salvar e Entrar',font=self.fonte,command=self.salvauser and self.vizualizaPres)
        self.botaosalva.place(x=920,y=250)
        self.botaosalva.config(relief='ridge',border=4,bd=2)
        self.labelmensagem = Label(text='', font=self.fonte)
        self.labelmensagem.place(x=920, y=300)
       
#FACILITA POSICAO NA TELA
     #   self.janela2.bind("<Button-1>",self.trataEvento)
        mainloop()
   # def trataEvento(self,event):
    #    print("voce clicou na posição",event.x,event.y)
        

        
    def salvauser(self):

        nome = self.caixanome.get()
        telefone = self.caixatelefone.get()
        cpf = self.caixacpf.get()
        email = self.caixaemail.get()
        usuario = self.caixausuario.get()
        senha = self.caixasenha.get()
        genero=self.comboGenero.get()
        endereco = self.enderecos.get(1.0,END)
        estado = self.comboestado.get()

        self.db.insert(nome, telefone, cpf, email, usuario, senha,genero,endereco, estado)
    def vizualizaPres(self):
        self.janela2.destroy()
        View()


       # messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
   

  


       
       



