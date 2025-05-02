class BuscarSerieNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_serie_nome(self):
        try:
            self.cursor.execute(
                "SELECT Title, Plot TEXT, Year, Genre, Rated, Runtime, Language, Country, Type, Seasons FROM Series WHERE Title ILIKE %s",
                (f"%{self.nome}%",)
            )
            return self.cursor.fetchall()
        except Exception:
            self.cursor.connection.rollback()
            return None
