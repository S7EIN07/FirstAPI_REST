class BuscarFilmeNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_filme_nome(self):
        try:
            self.cursor.execute("SELECT * FROM filmes WHERE nome ILIKE %s", (self.nome,))
            return self.cursor.fetchone()
        except Exception:
            self.cursor.connection.rollback()
            return None