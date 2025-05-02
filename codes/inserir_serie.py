class InserirSerie:
    def __init__(self, conn, resultado):
        self.conn = conn
        self.cursor = conn.cursor()
        self.resultado = resultado

    def inserir_no_bd(self):
        omdb_id = self.resultado.get("imdbID")
        title = self.resultado.get("Title")
        plot = self.resultado.get("Plot")
        year = self.resultado.get("Year")
        genre = self.resultado.get("Genre")
        rated = self.resultado.get("Rated")
        runtime = self.resultado.get("Runtime")
        language = self.resultado.get("Language")
        country = self.resultado.get("Country")
        type_filme_serie = self.resultado.get("Type")
        seasons = self.resultado.get("Seasons")

        print("Tentando inserir filme:", title, omdb_id)

        if type_filme_serie == "series":
            query = """
                INSERT INTO Series (Title, Plot, Year, Genre, Rated, Runtime, Language, Country, Type, Seasons, id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """
            with self.conn.cursor() as cursor:
                cursor.execute(query, (title, plot, year, genre, rated, runtime, language, country, type_filme_serie, seasons, omdb_id))
                self.conn.commit()
        elif type_filme_serie == "movie":
            from codes import inserir_filme
            inserir_new_filme = inserir_filme.InserirFilme(self.conn, self.resultado)
            inserir_new_filme.inserir_no_bd()
          