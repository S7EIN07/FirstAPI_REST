import requests

class BuscarOMDbFilmeNome:
    def __init__(self, cursor, nome_filme, API_KEY):
        self.cursor = cursor
        self.nome = nome_filme
        self.api_key = API_KEY

    def buscar_omdb_filme_nome(self):
        url_busca = f"https://www.omdbapi.com/?s={self.nome}&apikey={self.api_key}"
        resposta = requests.get(url_busca)

        if resposta.status_code != 200:
            return []

        dados = resposta.json()
        if dados.get("Response") != "True":
            return []

        resultados_completos = []
        for item in dados.get("Search", []):
            imdb_id = item.get("imdbID")
            if imdb_id:
                detalhes_url = f"https://www.omdbapi.com/?i={imdb_id}&apikey={self.api_key}"
                detalhes_resp = requests.get(detalhes_url)
                if detalhes_resp.status_code == 200:
                    detalhe = detalhes_resp.json()
                    if detalhe.get("Response") == "True":
                        resultados_completos.append(detalhe)

        return resultados_completos