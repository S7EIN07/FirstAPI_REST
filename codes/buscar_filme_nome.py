class BuscarFilmeNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_filme_nome(self):
        try:
            self.cursor.execute(
                "SELECT Title, Plot, Year, Genre, Rated, Runtime, Language, Country, Type FROM Filmes WHERE Title ILIKE %s",
                (f"%{self.nome}%",)
            )
            return self.cursor.fetchall()
        except Exception:
            self.cursor.connection.rollback()
            return None
