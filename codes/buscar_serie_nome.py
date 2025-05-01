class BuscarSerieNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_serie_nome(self):
        try:
            self.cursor.execute("SELECT * FROM series WHERE nome ILIKE %s", (self.nome,))
            return self.cursor.fetchone()
        except Exception:
            self.cursor.connection.rollback()
            return None