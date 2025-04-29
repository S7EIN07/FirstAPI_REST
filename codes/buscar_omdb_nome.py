class BuscarOMDbNome:
    def __init__(self, cursor, nome_filme, API_KEY):
        self.nome = nome_filme
        self.cursor = cursor
        self.api_key = API_KEY

    def buscar_filme_omdb_nome(self):
        filme = "https://www.omdbapi.com/?t={self.nome_filme}&apikey=self.{api_key}"
        return filme
    
    def postar_no_bd(filme):

        return