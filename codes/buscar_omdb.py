class BuscarOMDb:
    def __init__(self, nome_filme, id, API_KEY):
        self.nome = nome_filme
        self.api_key = API_KEY
        self.id = id

    def buscar_filme_omdb_nome(self):
        return "https://www.omdbapi.com/?t={self.nome_filme}&apikey=self.{api_key}"           