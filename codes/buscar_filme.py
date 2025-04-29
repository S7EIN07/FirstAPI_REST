class BuscarFilme:
    def __init__(self, cursor, nome, id):
        self.cursor = cursor
        self.nome = nome
        self.id = id

    def buscar_filme_nome(self):
        cursor = self.cursor()
        cursor.execute("SELECT * FROM filmes WHERE nome = %s", (self.nome))
        filmes = cursor.fetchall()
        cursor.close()
        return filmes
    
    def buscar_filme_id(self):
        cursor = self.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = %s", (self.id))
        filmes = cursor.fetchall() 
        cursor.close()
        return filmes
    
    