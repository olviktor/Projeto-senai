"""usar no futuro para exlusao de usuarios
 def excluir(self):
        item_selecionado = self.treeview.focus()
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            if tk.messagebox.askyesno("Excluir Usuário", f"Deseja excluir o usuário {valores[0]}?"):
                self.cursor.execute("DELETE FROM prestadores WHERE id=?", (valores[0], ))
                self.conexao.commit()
                self.treeview.delete(item_selecionado)
                tk.messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")

       

    def editar(self):
        item_selecionado = self.treeview.focus()
            
        if item_selecionado:
            valores = self.treeview.item(item_selecionado)["values"]
            tk.messagebox.showinfo("Editar Usuário", f"Nome: {valores[0]}\nEmail: {valores[1]}")
    def exibir(self):
        self.cursor.execute("SELECT id, nome, telefone, profissao FROM prestadores")
        usuarios = self.cursor.fetchall()

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for usuario in usuarios:
            self.treeview.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3]))"""