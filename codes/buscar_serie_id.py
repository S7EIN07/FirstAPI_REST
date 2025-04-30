class BuscarSerieId:
    def __init__(self, cursor, id):
        self.cursor = cursor
        self.id = id

    def buscar_serie_id(self):
        cursor = self.cursor.cursor()
        cursor.execute("SELECT * FROM series WHERE id = %s", (self.id))
        series = cursor.fetchall() 
        cursor.close()
        return series