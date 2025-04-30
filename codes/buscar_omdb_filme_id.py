from flask import request

class BuscarOMDbFilmeId:
    def __init__(self, cursor, id_filme, API_KEY):
        self.cursor = cursor
        self.api_key = API_KEY
        self.id = id_filme

    def buscar_filme_omdb_nome(self):
        filme = f"https://www.omdbapi.com/?i={self.id}&apikey={self.api_key}"
        resposta = request.get_json(filme)
        return resposta.json()
    
    def postar_no_bd(filme):

        return