from flask import request

class BuscarOMDbFilmeNome:
    def __init__(self, cursor, nome_filme, API_KEY):
        self.nome = nome_filme
        self.cursor = cursor
        self.api_key = API_KEY

    def buscar_filme_omdb_nome(self):
        filme = f"https://www.omdbapi.com/?t={self.nome}&apikey={self.api_key}"
        resposta = request.get(filme)
        return resposta.json()
    
    def postar_no_bd(filme):

        return