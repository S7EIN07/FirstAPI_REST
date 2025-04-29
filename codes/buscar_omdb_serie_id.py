class BuscarOMDbSerieId:
    def __init__(self, cursor, id_serie, API_KEY):
        self.cursor = cursor
        self.api_key = API_KEY
        self.id = id_serie

    def buscar_serie_omdb_nome(self):
        serie = "https://www.omdbapi.com/?i={self.id}&apikey=self.{api_key}"
        return serie
    
    def postar_no_bd(serie):

        return