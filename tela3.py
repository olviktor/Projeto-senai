import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class View:
    def __init__(self):
        self.conexao = sqlite3.connect(r'C:\Users\Jussara\OneDrive\Área de Trabalho\trabalho senia\prestadores.db')
        self.cursor = self.conexao.cursor()

        self.janela4 = tk.Tk()
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
        scrollbar = ttk.Scrollbar(self.janela4)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.treeview.yview)

        self.exibir()

        self.janela4.mainloop()  

    def exibir(self):
        self.cursor.execute("SELECT id, nome, telefone, profissao FROM prestadores")
        prestadores = self.cursor.fetchall()

    
        for prestador in prestadores:
            self.treeview.insert("", "end", values=(prestador[0], prestador[1], prestador[2], prestador[3]))

    def excluir(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            if tk.messagebox.askyesno("Excluir Usuário", f"Deseja excluir o usuário {valores[0]}?"):
                self.cursor.execute("DELETE FROM prestadores WHERE id=?", (valores[0],))
                self.conexao.commit()
                self.treeview.delete(item_selecionado)
                tk.messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")

    def editar(self):
        item_selecionado = self.treeview.focus()

        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            tk.messagebox.showinfo("Editar Usuário", f"Nome: {valores[0]}\nEmail: {valores[1]}")


t = View()
