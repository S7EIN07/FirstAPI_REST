from flask import requests

class BuscarOMDbFilmeNome:
    def __init__(self, cursor, nome_filme, API_KEY):
        self.cursor = cursor
        self.nome = nome_filme
        self.api_key = API_KEY

    def buscar_omdb_filme_nome(self):
        filme = f"https://www.omdbapi.com/?t={self.nome}&apikey={self.api_key}"
        resposta = requests.get_json(filme)
        return resposta.json()
    
    def postar_no_bd(filme):

        return