from flask import Flask, request, jsonify
import psycopg
import os
from dotenv import load_dotenv
from codes import buscar_filme_nome, buscar_filme_id, buscar_omdb_filme_id, buscar_omdb_filme_nome, buscar_serie_nome, buscar_serie_id


app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")  


conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)


imdb_search = ('omdbapi.com/')


@app.route("/buscar_filme_nome/<nome_filme_link>", methods=["GET"])
def buscar_filmes_endpoint_nome(nome_filme_link):
    cursor = conn

    nome = nome_filme_link

    filme = buscar_filme_nome.BuscarFilmeNome(cursor, nome)
    resultado = filme.buscar_filme_nome()
    if not resultado:
        filme_omdb = buscar_omdb_filme_nome.BuscarOMDbFilmeNome(cursor, nome, API_KEY)
        resultado = filme_omdb.buscar_filme_omdb_nome.BuscarOMDbFilmeNome()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_filme_id/<id_filme_link>", methods=["GET"])
def buscar_filmes_endpoint_id(id_filme_link):
    cursor = conn

    id_filme = id_filme_link

    filme = buscar_filme_id.BuscarFilmeId(cursor, id_filme)
    resultado = filme.buscar_filme_id()
    if not resultado:
        filme_omdb = buscar_omdb_filme_id.BuscarOMDbFilmeId(cursor, id_filme, API_KEY)
        resultado = filme_omdb.buscar_filem_omdb_id.BuscarOMDbFilmeId()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_serie_nome/<nome_serie_link>", methods=["GET"])
def buscar_serie_endpoint_nome(nome_serie_link):
    cursor = conn

    nome_serie = nome_serie_link

    serie = buscar_serie_nome.BuscarSerieNome(cursor, nome_serie)
    resultado = serie.buscar_serie_nome()
    if not resultado:
        serie_omdb = buscar_omdb_filme_nome.BuscarOMDbSerieNome(cursor, nome_serie, API_KEY)
        resultado = serie_omdb.buscar_serie_omdb_nome.BuscarOMDbSerieNome()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_serie_id/<id_serie_link>", methods=["GET"])
def buscar_serie_endpoint_id(id_serie_link):
    cursor = conn

    id_serie = id_serie_link

    serie = buscar_serie_nome.BuscarSerieId(cursor, id_serie)
    resultado = serie.buscar_serie()
    if not resultado:
        serie_omdb = buscar_omdb_filme_nome.BuscarOMDbSerieId(cursor, id_serie, API_KEY)
        resultado = serie_omdb.buscar_omdb.BuscarOMDbSerieId()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })