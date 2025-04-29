class BuscarSerie:
    def __init__(self, cursor, nome, id):
        self.cursor = cursor
        self.nome = nome
        self.id = id

    def buscar_serie_nome(self):
        cursor = self.cursor()
        cursor.execute("SELECT * FROM series WHERE nome = %s", (self.nome))
        series = cursor.fetchall() 
        cursor.close()
        return series
    
    def buscar_serie_id(self):
        cursor = self.cursor()
        cursor.execute("SELECT * FROM series WHERE id = %s", (self.id))
        series = cursor.fetchall() 
        cursor.close()
        return series