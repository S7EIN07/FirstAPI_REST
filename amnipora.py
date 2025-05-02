from flask import Flask, jsonify
import psycopg
import os
from dotenv import load_dotenv
from codes import (
    buscar_filme_nome, buscar_filme_id, buscar_omdb_filme_id, 
    buscar_omdb_filme_nome, buscar_serie_nome, buscar_serie_id, 
    buscar_omdb_serie_id, buscar_omdb_serie_nome, inserir_filme,
    inserir_serie
)


app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")  


conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)


@app.route("/filme/nome/<nome>", methods=["GET"])
def buscar_filmes_endpoint_nome(nome):
    conn.rollback()
    cursor = conn.cursor()
    nome = nome

    filme = buscar_filme_nome.BuscarFilmeNome(cursor, nome)
    resultados = filme.buscar_filme_nome()

    filmes_json = []

    if resultados:
        for resultado in resultados:
            filmes_json.append({
                "Titulo": resultado[1],
                "Plot": resultado[2],
                "Ano": resultado[3],
                "Genero": resultado[4],
                "Qualificação": resultado[5],
                "Duração": resultado[6],
                "Lingua": resultado[7],
                "Pais": resultado[8],
                "Tipo": resultado[9],
            })
    else:
        filme_omdb = buscar_omdb_filme_nome.BuscarOMDbFilmeNome(cursor, nome, API_KEY)
        resultados_omdb = filme_omdb.buscar_omdb_filme_nome()

        if not resultados_omdb:
            cursor.close()
            return jsonify({"erro": "Filme não encontrado."}), 404

        for resultado in resultados_omdb:
            title = resultado.get("Title")
            plot = resultado.get("Plot")
            year = resultado.get("Year")
            genre = resultado.get("Genre")
            rated = resultado.get("Rated")
            runtime = resultado.get("Runtime")
            language = resultado.get("Language")
            country = resultado.get("Country")
            type_filme_serie = resultado.get("Type")

            inserir_filme_endpoint = inserir_filme.InserirFilme(conn, resultado)
            inserir_filme_endpoint.inserir_no_bd()

            filmes_json.append({
                "Titulo": title,
                "Plot": plot,
                "Ano": year,
                "Genero": genre,
                "Qualificação": rated,
                "Duração": runtime,
                "Lingua(s)": language,
                "Pais(es)": country,
                "Tipo": type_filme_serie,
            })

    conn.commit()
    cursor.close()
    return jsonify(filmes_json)

@app.route("/filme/id/<id>", methods=["GET"])
def buscar_filmes_endpoint_id(id):
    conn.rollback()
    cursor = conn.cursor()
    id_filme = id

    filme = buscar_filme_id.BuscarFilmeId(cursor, id_filme)
    resultado = filme.buscar_filme_id()

    if resultado:
        title = resultado[1]
        plot = resultado[2]
        year = resultado[3]
        genre = resultado[4]
        rated = resultado[5]
        runtime = resultado[6]
        language = resultado[7]
        country = resultado[8]
        type_filme_serie = resultado[9]
    else:
        filme_omdb = buscar_omdb_filme_id.BuscarOMDbFilmeId(cursor, id_filme, API_KEY)
        resultado = filme_omdb.buscar_omdb_filme_id()

        if not resultado:
            return jsonify({"erro": "Filme não encontrado."}), 404

        title = resultado.get("Title")
        plot = resultado.get("Plot")
        year = resultado.get("Year")
        genre = resultado.get("Genre")
        rated = resultado.get("Rated")
        runtime = resultado.get("Runtime")
        language = resultado.get("Language")
        country = resultado.get("Country")
        type_filme_serie = resultado.get("Type")


        inserir_filme_endpoint = inserir_filme.InserirFilme(conn, resultado)
        inserir_filme_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": title,
        "Plot": plot,
        "Ano": year,
        "Genero": genre,
        "Qualificação": rated,
        "Duração": runtime,
        "Lingua(s)": language,
        "Pais(es)": country,
        "Série ou Filme": type_filme_serie
    })

    cursor.close()

    return jsonify({
        "Titulo": title,
        "Plot": plot,
        "Ano": year,
        "Genero": genre,
        "Qualificação": rated,
        "Duração": runtime,
        "Lingua(s)": language,
        "Pais(es)": country,
        "Série ou Filme": type_filme_serie
    })


@app.route("/serie/nome/<nome>", methods=["GET"])
def buscar_serie_endpoint_nome(nome):
    conn.rollback()
    cursor = conn.cursor()
    nome = nome

    serie = buscar_serie_nome.BuscarSerieNome(cursor, nome)
    resultados = serie.buscar_serie_nome()

    series_json = []

    if resultados:
        for resultado in resultados:
            series_json.append({
                "Titulo": resultado[1],
                "Plot": resultado[2],
                "Ano": resultado[3],
                "Genero": resultado[4],
                "Qualificação": resultado[5],
                "Duração": resultado[6],
                "Lingua": resultado[7],
                "Pais": resultado[8],
                "Tipo": resultado[9],
                "Temporadas": resultado[10],
            }), 200
    else:
        serie_omdb = buscar_omdb_serie_nome.BuscarOMDbSerieNome(cursor, nome, API_KEY)
        resultados_omdb = serie_omdb.buscar_omdb_serie_nome()

        if not resultados_omdb:
            cursor.close()
            return jsonify({"erro": "Serie não encontrado."}), 404

        for resultado in resultados_omdb:
            title = resultado.get("Title")
            plot = resultado.get("Plot")
            year = resultado.get("Year")
            genre = resultado.get("Genre")
            rated = resultado.get("Rated")
            runtime = resultado.get("Runtime")
            language = resultado.get("Language")
            country = resultado.get("Country")
            type_filme_serie = resultado.get("Type")
            seasons = resultado.get("Seasons")

            inserir_serie_endpoint = inserir_serie.InserirSerie(conn, resultado)
            inserir_serie_endpoint.inserir_no_bd()

            series_json.append({
                "Titulo": title,
                "Plot": plot,
                "Ano": year,
                "Genero": genre,
                "Qualificação": rated,
                "Duração": runtime,
                "Lingua(s)": language,
                "Pais(es)": country,
                "Tipo": type_filme_serie,
                "Temporadas": seasons,
            })

    conn.commit()
    cursor.close()
    return jsonify(series_json)


@app.route("/serie/id/<id>", methods=["GET"])
def buscar_serie_endpoint_id(id):
    conn.rollback()
    cursor = conn.cursor()
    id_serie = id

    serie = buscar_serie_id.BuscarSerieId(cursor, id_serie)
    resultado = serie.buscar_serie_id()

    if resultado:
        title = resultado[1]
        plot = resultado[2]
        year = resultado[3]
        genre = resultado[4]
        rated = resultado[5]
        runtime = resultado[6]
        language = resultado[7]
        country = resultado[8]
        type_filme_serie = resultado[9]
        seasons = resultado [10]
    else:
        serie_omdb = buscar_omdb_serie_id.BuscarOMDbSerieId(cursor, id_serie, API_KEY)
        resultado = serie_omdb.buscar_omdb_serie_id()

        if not resultado:
            return jsonify({"erro": "Série não encontrada."}), 404

        title = resultado.get("Title")
        plot = resultado.get("Plot")
        year = resultado.get("Year")
        genre = resultado.get("Genre")
        rated = resultado.get("Rated")
        runtime = resultado.get("Runtime")
        language = resultado.get("Language")
        country = resultado.get("Country")
        type_filme_serie = resultado.get("Type")
        seasons = resultado.get("Seasons")

        inserir_serie_endpoint = inserir_serie.InserirSerie(conn, resultado)
        inserir_serie_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": title,
        "Plot": plot,
        "Ano": year,
        "Genero": genre,
        "Qualificação": rated,
        "Duração": runtime,
        "Lingua(s)": language,
        "Pais(es)": country,
        "Temporadas": seasons,
        "Série ou Filme": type_filme_serie,
    })

    cursor.close()

    return jsonify({
        "Titulo": title,
        "Plot": plot,
        "Ano": year,
        "Genero": genre,
        "Qualificação": rated,
        "Duração": runtime,
        "Lingua(s)": language,
        "Pais(es)": country,
        "Temporadas": seasons,
        "Série ou Filme": type_filme_serie,
    })