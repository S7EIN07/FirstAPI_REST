class BuscarOMDbId:
    def __init__(self, cursor, id, API_KEY):
        self.cursor = cursor
        self.api_key = API_KEY
        self.id = id

    def buscar_filme_omdb_nome(self):
        filme = "https://www.omdbapi.com/?i={self.id}&apikey=self.{api_key}"
        return filme
    
    def postar_no_bd(filme):

        return