class BuscarSerie:
    def __init__(self, conn, nome, id):
        self.conn = conn
        self.nome = nome
        self.id = id

    def buscar_serie_nome(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM series WHERE nome = %s", (self.nome))
        series = cursor.fetchall() 
        cursor.close()
        return series
    
    def buscar_serie_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM series WHERE id = %s", (self.id))
        series = cursor.fetchall() 
        cursor.close()
        return series