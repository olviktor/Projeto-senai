import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from db import *


class Vizualizacliente:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conexao = sqlite3.connect(r'C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\clientes.db')
        self.cursor = self.conexao.cursor()
        self.janela4 = tk.Tk()
        self.botao1 = tk.Button(text='Configurações')
        self.botao1.place(x=0, y=0)
        self.botao1.config(relief="flat")
        self.botao2 = tk.Button(text='Perfil', command=self.ChamaPerfil)
        self.botao2.place(x=86, y=0)
        self.botao2.config(relief="flat")
        self.botao3 = tk.Button(text='Pagamento')
        self.botao3.place(x=123, y=0)
        self.botao3.config(relief="flat")
        self.botao4 = tk.Button(text='FAQ')
        self.botao4.place(x=190, y=0)
        self.botao4.config(relief="flat")
        self.caixaPesquisa = tk.Entry()
        self.caixaPesquisa.place(x=930, y=0)
        self.labelpesquisa = tk.Label(text="Pesquisar", bg='#ff8c00')
        self.labelpesquisa.place(x=870, y=0)

        style = ttk.Style()

        style.configure(
            "Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3"
        )
        style.map("Treeview", background=[('selected', 'orange')])

        self.janela4.title("LISTA DE CLIENTES DISPONIVEIS")
        self.janela4.config(bg='#ff8c00')
        self.treeview = ttk.Treeview(
            self.janela4, columns=("Id", "Nome", "Telefone"), show="headings", height=900
        )
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Telefone", text="Telefone")
        

        self.treeview.pack(fill=tk.X, pady=26)
        self.treeview.column("Id", width=10)
        self.treeview.column("Nome", width=300)
        self.treeview.column("Telefone", width=300)

        self.treeview.bind("<<TreeviewSelect>>", self.exibir_informacoes)
        self.caixaPesquisa.bind("<KeyRelease>", self.pesquisa)

        scrollbar = ttk.Scrollbar(self.janela4)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.treeview.yview)

        self.exibir()

        self.informacoes_frame = tk.Frame(self.janela4, bg='#7ac0d7')
        self.label_id = tk.Label(self.informacoes_frame, text="ID:", bg='#7ac0d7')
        self.label_nome = tk.Label(self.informacoes_frame, text="Nome:", bg='#7ac0d7')
        self.label_telefone = tk.Label(self.informacoes_frame, text="Telefone:", bg='#7ac0d7')
        self.label_profissao = tk.Label(self.informacoes_frame, text="Profissão:", bg='#7ac0d7')

        self.janela4.mainloop()

    def exibir(self):
        self.cursor.execute("SELECT id, nome, telefone, estado FROM clientes")
        clientes = self.cursor.fetchall()

        for clientes in clientes:
            self.treeview.insert("", "end", values=(clientes[0], clientes[1], clientes[2], clientes[3]))

    def exibir_informacoes(self, event):
        item_selecionado = self.treeview.focus()
        self.cursor.execute("SELECT id, nome, telefone,  estado FROM clientes")
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            escolha = messagebox.askyesno(
                "Informações do Cliente",
                f"Id: {valores[0]}\nNome: {valores[1]}\nTelefone: {valores[2]}\nEstado:{valores[3]}"
            )
            if escolha:
                None

    def pesquisa(self, event):
        texto_pesquisa = self.caixaPesquisa.get()
        self.treeview.delete(*self.treeview.get_children())  # Limpa a exibição atual

        self.cursor.execute("SELECT id, nome, telefone, estado FROM clientes WHERE nome LIKE ?",
                            ('%' + texto_pesquisa + '%',))
        prestadores = self.cursor.fetchall()

        for prestador in prestadores:
            self.treeview.insert(
                "", "end", values=(prestador[0], prestador[1], prestador[2], prestador[3])
            )
    def ChamaPerfil(self):
        from infopres import TelaExibirInformacoesProfissional
        self.janela4.destroy()
        TelaExibirInformacoesProfissional(self.user_id)
