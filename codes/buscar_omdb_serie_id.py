from flask import request

class BuscarOMDbSerieId:
    def __init__(self, cursor, id_serie, API_KEY):
        self.cursor = cursor
        self.api_key = API_KEY
        self.id = id_serie

    def buscar_serie_omdb_nome(self):
        serie = f"https://www.omdbapi.com/?i={self.id}&apikey={self.api_key}"
        resposta = request.get(serie)
        return resposta.json()
    
    def postar_no_bd(serie):

        return