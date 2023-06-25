import sqlite3

class Database:
    def __init__(self, db):
        #Criar a conexao com o banco
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
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
            estado TEXT
        )"""
        self.cursor.execute(sql)
        self.con.commit()

    def insert(self, nome, telefone, cpf, email, usuario, senha, genero, endereco, estado):
        self.cursor.execute(
            """INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (nome, telefone, cpf, email, usuario, senha, genero, endereco, estado)
        )
        self.con.commit()
        

    def update(self, id, nome, telefone, cpf, email, usuario, senha, genero, endereco, estado):
        self.cursor.execute(
            """UPDATE clientes SET nome=?, telefone=?, cpf=?, email=?, usuario=?, senha=?, genero=?, endereco=?, estado=? WHERE id=?""",
            (nome, telefone, cpf, email, usuario, senha, genero, endereco, estado,id)
        )
        self.con.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
        self.con.commit()

    def fetch_by_id(self, id):
        self.cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
        row = self.cursor.fetchone()
        if row:
            data = {
                'id': row[0],
                'nome': row[1],
                'telefone': row[2],
                'cpf': row[3],
                'email': row[4],
                'usuario': row[5],
                'senha': row[6],
                'genero': row[7],
                'endereco': row[8],
                'estado': row[9]
            }
            return data
        else:
            return None

    def obter_id_cliente_por_usuario(self, usuario):
        query = "SELECT id FROM clientes WHERE usuario = ?"
        params = (usuario,)
        self.cursor.execute(query, params)
        row = self.cursor.fetchone()
        if row:
            return row['id']
        else:
            return None

    def verificaLogin(self, usuario, senha):
        query = "SELECT * FROM clientes WHERE usuario = ? AND senha = ?"
        params = (usuario, senha)
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
    def get_last_inserted_id(self):
        self.cursor.execute("SELECT last_insert_rowid()")
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None


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
            profissao TEXT
            )"""
        #Executando o comando acima
        self.cursor.execute(sql)
        #Persistindo o que foi feito
        self.con.commit()

    def insertpres(self, nome, telefone, cpf, email, usuario, senha, genero, endereco, estado,profissao):
        self.cursor.execute(
            """INSERT INTO prestadores VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (nome, telefone, cpf, email, usuario, senha, genero, endereco, estado, profissao)
        )
        self.con.commit()

    def updatepres(self,id, nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao):
        #edita UM FUNCIONÁRIO NA TABELA
        self.cursor.execute("""UPDATE prestadores SET 
                     nome=?, telefone=?, cpf=?, email=?, usuario=?,senha=?, genero=?,endereco=?,estado=?,profissao=? WHERE id=?""",
         (nome,telefone,cpf,email,usuario,senha,genero,endereco,estado,profissao,id))
        #Persistindo o que foi feito
        self.con.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM prestadores WHERE id=?", (id,))
        self.con.commit()
       

    def fetch(self):
        self.cursor.execute("SELECT * FROM prestadores")
        rows = self.cursor.fetchall()
        return rows
    

    def obter_id_cliente_por_usuario(self, usuario):
        query = "SELECT id FROM prestadores WHERE usuario = ?"
        params = (usuario,)
        self.cursor.execute(query, params)
        row = self.cursor.fetchone()
        if row:
            return row['id']
        else:
            return None

    def verificaLoginpres(self, usuario, senha):
        query = "SELECT * FROM prestadores WHERE usuario = ? AND senha = ?"
        params = (usuario, senha)
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
    def get_last_inserted_idpres(self):
        self.cursor.execute("SELECT last_insert_rowid()")
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None
    def fetch_by_idpres(self, id):
        self.cursor.execute("SELECT * FROM prestadores WHERE id=?", (id,))
        row = self.cursor.fetchone()
        if row:
            data = {
                'id': row[0],
                'nome': row[1],
                'telefone': row[2],
                'cpf': row[3],
                'email': row[4],
                'usuario': row[5],
                'senha': row[6],
                'genero': row[7],
                'endereco': row[8],
                'estado': row[9],
                'profissao':row[10]
            }
            return data
        else:
            return None