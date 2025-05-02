class BuscarSerieId:
    def __init__(self, cursor, id_serie):
        self.cursor = cursor
        self.id_serie = id_serie

    def buscar_serie_id(self):
        try:
            self.cursor.execute("SELECT Title, Plot TEXT, Year, Genre, Rated, Runtime, Language, Country, Type, Seasons FROM Series WHERE id = %s", (self.id_serie,))
            return self.cursor.fetchone()
        except Exception:
            self.cursor.connection.rollback()
            return None