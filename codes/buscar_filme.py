class BuscarFilme:
    def __init__(self, conn, nome, id):
        self.conn = conn
        self.nome = nome
        self.id = id

    def buscar_filme(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes WHERE nome = %s", (self.nome))
        filmes = cursor.fetchall() 
        cursor.close()
        return filmes