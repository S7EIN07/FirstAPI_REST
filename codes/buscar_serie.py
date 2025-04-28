class BuscarSerie:
    def __init__(self, conn):
        self.conn = conn

    def buscar_serie(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM series")
        series = cursor.fetchall()  # Captura os dados do SELECT
        cursor.close()
        return series