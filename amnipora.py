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


@app.route("/buscar_filme_nome/<nome_filme_link>", methods=["GET"])
def buscar_filmes_endpoint_nome(nome_filme_link):
    conn.rollback()
    cursor = conn.cursor()
    nome = nome_filme_link

    filme = buscar_filme_nome.BuscarFilmeNome(cursor, nome)
    resultado = filme.buscar_filme_nome()

    if resultado:
        titulo = resultado[1]
        ano = resultado[2]
        genero = resultado[3]
    else:
        filme_omdb = buscar_omdb_filme_nome.BuscarOMDbFilmeNome(cursor, nome, API_KEY)
        resultado = filme_omdb.buscar_omdb_filme_nome()

        if not resultado:  # OMDb não retornou nada
            cursor.close()
            return jsonify({"erro": "Filme não encontrado."}), 404

        titulo_omdb = resultado.get("Title")
        ano_omdb = resultado.get("Year")
        genero_omdb = resultado.get("Genre")
        tipo_omdb = resultado.get("Type")
        if tipo_omdb == "movie":
            tipo_omdb = "Filme"
        elif tipo_omdb == "series":
            tipo_omdb = "Série"

        inserir_filme_endpoint = inserir_filme.InserirFilme(conn, resultado)
        inserir_filme_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": titulo_omdb,
        "Ano": ano_omdb,
        "Genero": genero_omdb,
        "Filme ou Série": tipo_omdb,
        "mensagem": "Postado no banco de dados"
    })

    cursor.close()

    return jsonify({
        "Titulo": titulo,
        "Ano": ano,
        "Genero": genero,
        "mensagem": "Buscado no bando de dados"
    })


@app.route("/buscar_filme_id/<id_filme_link>", methods=["GET"])
def buscar_filmes_endpoint_id(id_filme_link):
    conn.rollback()
    cursor = conn.cursor()
    id_filme = id_filme_link

    filme = buscar_filme_id.BuscarFilmeId(cursor, id_filme)
    resultado = filme.buscar_filme_id()

    if resultado:
        titulo = resultado[1]
        ano = resultado[2]
        genero = resultado[3]
    else:
        filme_omdb = buscar_omdb_filme_id.BuscarOMDbFilmeId(cursor, id_filme, API_KEY)
        resultado = filme_omdb.buscar_omdb_filme_id()

        if not resultado:
            return jsonify({"erro": "Filme não encontrado."}), 404

        titulo_omdb = resultado.get("Title")
        ano_omdb = resultado.get("Year")
        genero_omdb = resultado.get("Genre")
        tipo_omdb = resultado.get("Type")

        inserir_filme_endpoint = inserir_filme.InserirFilme(conn, resultado)
        inserir_filme_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": titulo_omdb,
        "Ano": ano_omdb,
        "Genero": genero_omdb,
        "Filme ou Série": tipo_omdb,
        "mensagem": "Postado no banco de dados"
    })

    cursor.close()

    return jsonify({
        "Titulo": titulo,
        "Ano": ano,
        "Genero": genero,
        "mensagem": "Buscado no bando de dados"
    })


@app.route("/buscar_serie_nome/<nome_serie_link>", methods=["GET"])
def buscar_serie_endpoint_nome(nome_serie_link):
    conn.rollback()
    cursor = conn.cursor()
    nome_serie = nome_serie_link

    serie = buscar_serie_nome.BuscarSerieNome(cursor, nome_serie)
    resultado = serie.buscar_serie_nome()

    if resultado:
        titulo = resultado[1]
        ano = resultado[2]
        genero = resultado[3]
    else:
        serie_omdb = buscar_omdb_serie_nome.BuscarOMDbSerieNome(cursor, nome_serie, API_KEY)
        resultado = serie_omdb.buscar_omdb_serie_nome()

        if not resultado:
            return jsonify({"erro": "Série não encontrada."}), 404

        titulo_omdb = resultado.get("Title")
        ano_omdb = resultado.get("Year")
        genero_omdb = resultado.get("Genre")
        tipo_omdb = resultado.get("Type")

        inserir_serie_endpoint = inserir_serie.InserirSerie(conn, resultado)
        inserir_serie_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": titulo_omdb,
        "Ano": ano_omdb,
        "Genero": genero_omdb,
        "Filme ou Série": tipo_omdb,
        "mensagem": "Postado no banco de dados"
    })
    cursor.close()

    return jsonify({
        "Titulo": titulo,
        "Ano": ano,
        "Genero": genero,
        "mensagem": "Buscado no bando de dados"
    })


@app.route("/buscar_serie_id/<id_serie_link>", methods=["GET"])
def buscar_serie_endpoint_id(id_serie_link):
    conn.rollback()
    cursor = conn.cursor()
    id_serie = id_serie_link

    serie = buscar_serie_id.BuscarSerieId(cursor, id_serie)
    resultado = serie.buscar_serie_id()

    if resultado:
        titulo = resultado[1]
        ano = resultado[2]
        genero = resultado[3]
    else:
        serie_omdb = buscar_omdb_serie_id.BuscarOMDbSerieId(cursor, id_serie, API_KEY)
        resultado = serie_omdb.buscar_omdb_serie_id()

        if not resultado:
            return jsonify({"erro": "Série não encontrada."}), 404

        titulo_omdb = resultado.get("Title")
        ano_omdb = resultado.get("Year")
        genero_omdb = resultado.get("Genre")
        tipo_omdb = resultado.get("Type")

        inserir_serie_endpoint = inserir_serie.InserirSerie(conn, resultado)
        inserir_serie_endpoint.inserir_no_bd()

        return jsonify({
        "Titulo": titulo_omdb,
        "Ano": ano_omdb,
        "Genero": genero_omdb,
        "Filme ou Série": tipo_omdb,
        "mensagem": "Postado no banco de dados"
    })

    cursor.close()

    return jsonify({
        "Titulo": titulo,
        "Ano": ano,
        "Genero": genero,
        "mensagem": "Buscado no bando de dados"
    })