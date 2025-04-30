import requests

class BuscarOMDbFilmeNome:
    def __init__(self, cursor, nome_filme, API_KEY):
        self.cursor = cursor
        self.nome = nome_filme
        self.api_key = API_KEY

    def buscar_omdb_filme_nome(self):
        url = f"https://www.omdbapi.com/?t={self.nome}&apikey={self.api_key}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "Não foi possível obter os dados do filme"}

    def postar_no_bd(self, filme):
        # Implementar lógica para salvar o filme no banco de dados
        pass