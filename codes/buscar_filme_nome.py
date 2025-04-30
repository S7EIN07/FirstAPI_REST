class BuscarFilmeNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_filme_nome(self):
        cursor = self.cursor.cursor()
        cursor.execute("SELECT * FROM filmes WHERE nome = %s", (self.nome))
        filmes = cursor.fetchall()
        cursor.close()
        return filmes
    
    
    
    