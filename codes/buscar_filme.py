from flask import jsonify


class BuscarFilme():
    def __init__(self, nome_do_filme, ano_do_filme):
        self.nome_do_filme = nome_do_filme
        self.ano_do_filme = ano_do_filme

    def buscar_filme():
        return jsonify({'message': 'filme buscado'})