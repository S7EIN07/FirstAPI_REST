from flask import jsonify


class BuscarSerie():
    def __init__(self, nome_do_serie, ano_do_serie):
        self.nome_do_serie = nome_do_serie
        self.ano_do_serie = ano_do_serie
        
    def buscar_serie():
        return jsonify({'message': 'serie buscado'})