import requests

class BuscarOMDbserieNome:
    def __init__(self, cursor, nome_serie, API_KEY):
        self.nome = nome_serie
        self.cursor = cursor
        self.api_key = API_KEY

    def buscar_serie_omdb_nome(self):
        serie = f"https://www.omdbapi.com/?t={self.nome}&apikey={self.api_key}"
        resposta = requests.get(serie)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "Falha ao obter os dados da API"}
    
    def postar_no_bd(serie):

        return