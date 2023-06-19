import sqlite3

class Database:
    def __init__(self, db):
        #Criar a conexao com o banco
        self.con = sqlite3.connect(db)
        #Cria um cursor para realizar as operações no banco
        self.cursor = self.con.cursor()
        #Cria a tabela de funcionários
        sql = """CREATE TABLE IF NOT EXISTS clientes(
id INTEGER PRIMARY KEY,
nome TEXT,
telefone INTEGER,
cpf TEXT,
email TEXT,
usuario TEXT,
senha TEXT,
genero TEXT,
endereco TEXT,
estado TEXT)"""
        #Executando o comando acima
        self.cursor.execute(sql)
        #Persistindo o que foi feito
        self.con.commit()

    def insert(self, nome,telefone,cpf,email,usuario,senha,genero,endereco,estado):
        #ADICIONA UM FUNCIONÁRIO NA TABELA
        self.cursor.execute("""INSERT INTO clientes VALUES
(NULL, ?,?,?, ?, ?, ?, ?, ?, ?)""",
                            (nome,telefone,cpf,email,usuario,senha,genero,endereco,estado))
        #Persistindo o que foi feito
        self.con.commit()

    def update(self, nome,telefone,cpf,email,usuario,senha,genero,endereco,estado):
        #edita UM FUNCIONÁRIO NA TABELA
        self.cursor.execute("""UPDATE clientes SET nome=?, telefone=?,
cpf=?, email=?, usuario=?,senha=?, genero=?,endereco=?,estado=? WHERE id=?""",
                    (nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,id))
        #Persistindo o que foi feito
        self.con.commit()

    def remove(self, id):
        #remove um funcionário da tabela
        self.cursor.execute("DELETE FROM clientes WHERE id=?", (id, ))
        #Persistindo o que foi feito
        self.con.commit()

    def fetch(self):
        #Seleciona os funcionários da tabela
        self.cursor.execute("SELECT * FROM clientes")
        #salva os funcionarios na lista
        linhas = self.cursor.fetchall()
        #retorna a lista
        return linhas
    def verificaLogin(self,usuario,senha):
       query = "SELECT * FROM clientes WHERE usuario = ? AND senha = ?"
       params=(usuario,senha)
       self.cursor.execute(query,params)
       result=self.cursor.fetchone()
       if result:
          return True
       else:
           return False
       
class Prestadores:
    def __init__(self, db):
        #Criar a conexao com o banco
        self.con = sqlite3.connect(db)
        #Cria um cursor para realizar as operações no banco
        self.cursor = self.con.cursor()
        #Cria a tabela de funcionários
        sql = """CREATE TABLE IF NOT EXISTS prestadores(
id INTEGER PRIMARY KEY,
nome TEXT,
telefone INTEGER,
cpf TEXT,
email TEXT,
usuario TEXT,
senha TEXT,
genero TEXT,
endereco TEXT,
estado TEXT,
profissao TEXT,
descricao TEXT)"""
        #Executando o comando acima
        self.cursor.execute(sql)
        #Persistindo o que foi feito
        self.con.commit()

    def insertPres(self, nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao,descricao):
        #ADICIONA UM FUNCIONÁRIO NA TABELA
        self.cursor.execute("""INSERT INTO prestadores VALUES
(NULL, ?,?,?, ?, ?, ?, ?, ?, ?,?,?)""",
                            (nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao,descricao))
        #Persistindo o que foi feito
        self.con.commit()

    def update(self, nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao):
        #edita UM FUNCIONÁRIO NA TABELA
        self.cursor.execute("""UPDATE profissao SET nome=?, telefone=?,
cpf=?, email=?, usuario=?,senha=?, genero=?,endereco=?,estado=?,profissao=? WHERE id=?""",
                    (nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao,id))
        #Persistindo o que foi feito
        self.con.commit()

    def remove(self, id):
        #remove um funcionário da tabela
        self.cursor.execute("DELETE FROM prestadores WHERE id=?", (id, ))
        #Persistindo o que foi feito
        self.con.commit()

    def fetch(self):
        #Seleciona os funcionários da tabela
        self.cursor.execute("SELECT * FROM clientes")
        #salva os funcionarios na lista
        linhas = self.cursor.fetchall()
        #retorna a lista
        return linhas
    def verificaLogin(self,usuario,senha):
       query = "SELECT * FROM clientes WHERE usuario = ? AND senha = ?"
       params=(usuario,senha)
       self.cursor.execute(query,params)
       result=self.cursor.fetchone()
       if result:
          return True
       else:
           return False

  
       