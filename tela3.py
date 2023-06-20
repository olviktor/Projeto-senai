import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class View:
    def __init__(self):
        self.conexao = sqlite3.connect(r'C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\prestadores.db')
        self.cursor = self.conexao.cursor()
        self.janela4 =tk.Tk()
        style = ttk.Style()
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map("Treeview",
                  background=[('selected', '#347083')])
        self.janela4.title("LISTA DE PROFISSIONAIS DISPONIVEIS")
        self.janela4.config(bg='#7ac0d7')
        self.treeview = ttk.Treeview(self.janela4, columns=("Id", "Nome", "Telefone", "Profissão"), show="headings", height=900)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Telefone", text="Telefone")
        self.treeview.heading("Profissão", text="Profissão")
        
        self.treeview.pack(fill=tk.X)
        self.treeview.column("Id", width=10)
        self.treeview.column("Nome", width=300)
        self.treeview.column("Telefone", width=300)
        self.treeview.column("Profissão", width=300)
      
        self.treeview.bind("<<TreeviewSelect>>", self.exibir_informacoes)

        scrollbar = ttk.Scrollbar(self.janela4)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.treeview.yview)

        self.exibir()
       

        self.janela4.mainloop()  

    def exibir(self):
        self.cursor.execute("SELECT id, nome, telefone, profissao,estado FROM prestadores")
        prestadores = self.cursor.fetchall()

    
        for prestador in prestadores:
            self.treeview.insert("", "end", values=(prestador[0], prestador[1], prestador[2], prestador[3],prestador[4]))

   
    def exibir_informacoes(self, event):
        item_selecionado = self.treeview.focus()
        self.cursor.execute("SELECT id, nome, telefone, profissao, estado FROM prestadores")
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            # Exiba as informações do prestador selecionado
            tk.messagebox.showinfo("Informações do Prestador", f"Id: {valores[0]}\nNome: {valores[1]}\nTelefone: {valores[2]}\nProfissão: {valores[3]}\nEstado:{valores[4]}")

    
    


t = View()
