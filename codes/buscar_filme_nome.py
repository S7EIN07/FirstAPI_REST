class BuscarFilmeNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_filme_nome(self):
        self.cursor.execute("SELECT * FROM filmes WHERE nome = %s", (self.nome,))
        return self.cursor.fetchone()