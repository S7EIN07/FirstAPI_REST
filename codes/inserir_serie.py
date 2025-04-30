import json
from codes import inserir_filme

class InserirSerie:
    def __init__(self, conn, resultado):
        self.conn = conn
        self.cursor = conn.cursor()
        self.resultado = resultado

    def inserir_no_bd(self):
        omdb_id = self.resultado.get("imdbID")
        titulo = self.resultado.get("Title")
        ano = self.resultado.get("Year")
        genero = self.resultado.get("Genre")
        tipo = self.resultado.get("Type")
        dados = self.resultado

        if tipo == "series":
            query = """
                INSERT INTO series (omdb_id, nome, ano, genero, dados)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """
            self.cursor.execute(query, (omdb_id, titulo, ano, genero, json.dumps(dados)))
            with self.conn.cursor() as cursor:
                cursor.execute(query, (omdb_id, titulo, ano, genero, json.dumps(dados)))
        elif tipo == "movie":
            inserir_new_filme = inserir_filme.InserirSerie(self.conn, self.resultado)
            inserir_new_filme.inserir_no_bd()