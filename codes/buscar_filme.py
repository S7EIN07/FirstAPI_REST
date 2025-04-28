class BuscarFilme:
    def __init__(self, conn):
        self.conn = conn

    def buscar_filme(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes")
        filmes = cursor.fetchall() 
        cursor.close()
        return filmes