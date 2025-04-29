class BuscarFilme:
    def __init__(self, conn, nome, id):
        self.conn = conn
        self.nome = nome
        self.id = id

    def buscar_filme_nome(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes WHERE nome = %s", (self.nome))
        filmes = cursor.fetchall()
        cursor.close()
        return filmes
    
    def buscar_filme_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = %s", (self.id))
        filmes = cursor.fetchall() 
        cursor.close()
        return filmes
    
    