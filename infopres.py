from tkinter import *
from tkinter import ttk
from db import Prestadores
from tkinter import messagebox
from exibepres import Vizualiza




class TelaExibirInformacoesProfissional:
    def __init__(self, user_id):
        self.db = Prestadores(r"C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\prestadores.db")
        self.janela6 = Tk()
        self.fonte = ('Courier New', 12)
        dados = self.db.fetch_by_id(user_id)
        self.labelcor = Label(bg='#7ac0d7',width=200, height=200)
        self.labelcor.pack()
        # textos
        self.titulo = Label(text='Meu Perfil', font=('Courier New', 30))
        self.titulo.place(x=0, y=0)

        # LABEL INFOS
        self.labelnome = Label(text='Nome', font=self.fonte,bg='#7ac0d7')
        self.labelnome.place(x=50, y=200)
        self.labelnome.config(relief='flat')
        self.labelTelefone = Label(text='Telefone', font=self.fonte,bg='#7ac0d7')
        self.labelTelefone.place(x=50, y=250)
        self.labelcpf = Label(text='CPF', font=self.fonte,bg='#7ac0d7')
        self.labelcpf.place(x=50, y=300)
        self.labelemail = Label(text='Email', font=self.fonte,bg='#7ac0d7')
        self.labelemail.place(x=50, y=350)
        self.labelusuario = Label(text='Usuario', font=self.fonte,bg='#7ac0d7')
        self.labelusuario.place(x=50, y=400)
        self.labelsenha = Label(text='Senha', font=self.fonte,bg='#7ac0d7')
        self.labelsenha.place(x=50, y=450)
        self.genero1 = Label(text='Genero',bg='#7ac0d7')
        self.genero1.place(x=50, y=500)
        self.endereco = Label(text='Endereço', font=('Courier New', 12),bg='#7ac0d7')
        self.endereco.place(x=720, y=180)

        # CAIXAS INFOS
        self.caixanome = Entry(width=50)
        self.caixanome.place(x=150, y=200)
        self.caixanome.config(relief='groove', bd=1)
        self.caixanome.insert(0, dados['nome'])
        self.caixatelefone = Entry(width=50)
        self.caixatelefone.place(x=150, y=250)
        self.caixatelefone.config(relief='groove', bd=1)
        self.caixatelefone.insert(0, dados['telefone'])
        self.caixacpf = Entry(width=50)
        self.caixacpf.place(x=150, y=300)
        self.caixacpf.config(relief='groove', bd=1)
        self.caixacpf.insert(0, dados['cpf'])
        self.caixaemail = Entry(width=47)
        self.caixaemail.place(x=150, y=350)
        self.caixaemail.config(relief='groove', bd=1)
        self.caixaemail.insert(0, dados['email'])
        self.caixausuario = Entry(width=30, state='disabled')
        self.caixausuario.place(x=150, y=400)
        self.caixausuario.config(relief='flat', bd=2)
        self.caixausuario.insert(0, dados['usuario'])
        self.caixasenha = Entry(width=30, state='disabled')
        self.caixasenha.place(x=150, y=450)
        self.caixasenha.config(relief='flat', bd=2)
        self.caixasenha.insert(0, dados['senha'])
        self.comboGenero = ttk.Combobox(font=self.fonte, width=10)
        self.comboGenero['values'] = ("Masculino", 'Feminino', "Outro")
        self.comboGenero.place(x=150, y=500)
        self.comboGenero.set(dados['genero'])
        self.enderecos = Text(width=40, height=1)
        self.enderecos.place(x=720, y=200)
        self.enderecos.insert("1.0", dados['endereco'])
        self.comboestado = ttk.Combobox(font=self.fonte, width=2)
        self.comboestado['values'] = ('BA', 'SE', 'CE')
        self.comboestado.place(x=1050, y=200)
        self.comboestado.set(dados['estado'])
        self.comboprofissao = ttk.Combobox(font=self.fonte, state='readonly', width=6)
        self.comboprofissao['values'] = ('Pedreiro', 'Pintor', 'Carpinteiro')
        self.comboprofissao.place(x=820, y=300)
        self.comboestado.set(dados['profissao'])
        

        # BOTOES
        self.botaosalva = Button(text='Salvar', font=self.fonte, command=lambda: self.salvar_dadospres(user_id))
        self.botaosalva.place(x=920, y=250)
        self.botaosalva.config(relief='ridge', border=4, bd=0)
        self.botaoEditar = Button(text='Editar', font=self.fonte, command=self.habilitar_edicaopres)
        self.botaoEditar.place(x=820, y=250)
        self.botaoEditar.config(relief='ridge', border=4, bd=0)
        self.botaoDelete=Button(text='Apagar conta',font=self.fonte,command=lambda:self.deletarpres(user_id))
        self.botaoDelete.place(x=720,y=450)

        mainloop()

    def habilitar_edicaopres(self):
        self.caixanome.config(state='normal')
        self.caixatelefone.config(state='normal')
        self.caixacpf.config(state='normal')
        self.caixaemail.config(state='normal')
        self.caixausuario.config(state='normal',relief='raised')
        self.caixasenha.config(state='normal',relief='raised')
        self.comboGenero.config(state='readonly')
        self.enderecos.config(state='normal')
        self.comboestado.config(state='readonly')

    def salvar_dadospres(self, user_id):
        nome = self.caixanome.get()
        telefone = self.caixatelefone.get()
        cpf = self.caixacpf.get()
        email = self.caixaemail.get()
        usuario = self.caixausuario.get()
        senha = self.caixasenha.get()
        genero = self.comboGenero.get()
        endereco = self.enderecos.get("1.0", END)
        estado = self.comboestado.get()
        profissao=self.comboprofissao.get()

        if nome and telefone and cpf and email and  genero and endereco and estado and profissao:
            self.db.updatepres(user_id, nome, telefone, cpf, email, usuario, senha, genero, endereco, estado,profissao)
            messagebox.showinfo("Tudo certo",'Dados atualizados com sucesso!')
        else:
           messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos!")
    def deletarpres(self, user_id):
         from main import Tk
         self.db.remove(user_id)
         messagebox.showinfo("Sucesso", "Conta excluida")
         self.janela6.destroy()
         Tk

# ... código anterior ...

