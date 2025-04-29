class BuscarFilmeId:
    def __init__(self, cursor, id):
        self.cursor = cursor
        self.id = id

def buscar_filme_id(self):
        cursor = self.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = %s", (self.id))
        filmes = cursor.fetchall() 
        cursor.close()
        return filmes