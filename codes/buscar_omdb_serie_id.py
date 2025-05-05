import requests

class BuscarOMDbSerieId:
    def __init__(self, cursor, id_serie, API_KEY):
        self.cursor = cursor
        self.api_key = API_KEY
        self.id_serie = id_serie

    def buscar_omdb_serie_id(self):
        serie = f"https://www.omdbapi.com/?i={self.id_serie}&apikey={self.api_key}"
        resposta = requests.get(serie)
        if resposta.status_code == 200:
            return resposta.json()
            
        else:
            return {"erro": "Falha ao obter os dados da API"}