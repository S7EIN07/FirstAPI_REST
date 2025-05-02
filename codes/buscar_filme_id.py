class BuscarFilmeId:
    def __init__(self, cursor, id_filme):
        self.cursor = cursor
        self.id_filme = id_filme

    def buscar_filme_id(self):
        try:
            self.cursor.execute("SELECT Title, Plot TEXT, Year, Genre, Rated, Runtime, Language, Country, Type FROM Filmes WHERE omdb_id = %s", (self.id_filme,))
            return self.cursor.fetchone()
        except Exception:
            self.cursor.connection.rollback()
            return None