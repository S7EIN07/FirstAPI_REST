from flask import  jsonify

class MostrarDados:
    def __init__(self, conn, API_KEY):
        self.conn = conn
        self.cursor = conn.cursor()   
        self.API_KEY = API_KEY
        self.tipo = tipo 
        self.identificador = identificador
        self.buscar_local_func = buscar_local_func
        self.buscar_omdb_func = buscar_omdb_func
        self.inserir_func = inserir_func
        self.campos_adicionais = campos_adicionais
        
        
        
    def buscar_item(
        self,
        tipo: str,
        identificador: str,
        valor: str,
        buscar_local_func,
        buscar_omdb_func,
        inserir_func,
        campos_adicionais=[]
    ):
        self.conn.rollback()
        cursor = self.cursor

        item_local = buscar_local_func(cursor, valor)
        resultados = item_local() if identificador == "nome" else item_local

        if resultados:
            if isinstance(resultados, list):
                itens_json = []
                for resultado in resultados:
                    item_json = {
                        "Titulo": resultado[0],
                        "Plot": resultado[1],
                        "Ano": resultado[2],
                        "Genero": resultado[3],
                        "Classificação Indicativa": resultado[4],
                        "Duração": resultado[5],
                        "Lingua(s)": resultado[6],
                        "Pais(es)": resultado[7],
                        "Tipo": resultado[8],
                        "msg": "Busca no DB"
                    }
                    for i, campo in enumerate(campos_adicionais, start=9):
                        item_json[campo] = resultado[i]
                    itens_json.append(item_json)
                cursor.close()
                return jsonify(itens_json)

            else:
                resultado = resultados
                item_json = {
                    "Titulo": resultado[0],
                    "Plot": resultado[1],
                    "Ano": resultado[2],
                    "Genero": resultado[3],
                    "Classificação Indicativa": resultado[4],
                    "Duração": resultado[5],
                    "Lingua(s)": resultado[6],
                    "Pais(es)": resultado[7],
                    "Série ou Filme": resultado[8],
                    "msg": "Busca no DB"
                }
                for i, campo in enumerate(campos_adicionais, start=9):
                    item_json[campo] = resultado[i]
                cursor.close()
                return jsonify(item_json)

        item_omdb = buscar_omdb_func(cursor, valor, self.API_KEY)
        resultados_omdb = item_omdb() if identificador == "nome" else item_omdb

        if not resultados_omdb:
            cursor.close()
            return jsonify({"erro": f"{tipo.capitalize()} não encontrado."}), 404

        itens_json = []

        resultados = resultados_omdb if isinstance(resultados_omdb, list) else [resultados_omdb]

        for resultado in resultados:
            inserir_endpoint = inserir_func(self.conn, resultado)
            inserir_endpoint.inserir_no_bd()

            item_json = {
                "Titulo": resultado.get("Title"),
                "Plot": resultado.get("Plot"),
                "Ano": resultado.get("Year"),
                "Genero": resultado.get("Genre"),
                "Classificação Indicativa": resultado.get("Rated"),
                "Duração": resultado.get("Runtime"),
                "Lingua(s)": resultado.get("Language"),
                "Pais(es)": resultado.get("Country"),
                "Série ou Filme": resultado.get("Type"),
                "msg": "Buscado na OMDB e postado no BD"
            }
            for campo in campos_adicionais:
                item_json[campo] = resultado.get(campo)
            itens_json.append(item_json)

        self.conn.commit()
        cursor.close()

        return jsonify(itens_json[0] if identificador == "id" else itens_json)
