class BuscarSerieNome:
    def __init__(self, cursor, nome):
        self.cursor = cursor
        self.nome = nome

    def buscar_serie_nome(self):
        cursor = self.cursor
        cursor.execute("SELECT * FROM series WHERE nome = %s", (self.nome))
        series = cursor.fetchall() 
        cursor.close()
        return series
    
    