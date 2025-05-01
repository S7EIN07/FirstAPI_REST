import requests

class BuscarOMDbFilmeId:
    def __init__(self, cursor, id_filme, API_KEY):
        self.cursor = cursor
        self.id_filme = id_filme
        self.api_key = API_KEY

    def buscar_omdb_filme_id(self):
        filme = f"https://www.omdbapi.com/?i={self.id_filme}&apikey={self.api_key}"
        resposta = requests.get(filme)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "Falha ao obter os dados da API"}