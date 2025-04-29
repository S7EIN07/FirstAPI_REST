from flask import Flask, request, jsonify
import psycopg
import os
from dotenv import load_dotenv
from codes import buscar_serie, buscar_filme


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
def buscar_filmes_endpoint(nome_filme_link):
    cursor = conn

    nome = nome_filme_link

    filme = buscar_filme.BuscarFilme(cursor, nome)
    resultado = filme.buscar_filme()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_filme_id/<id_filme_link>", methods=["GET"])
def buscar_filmes_endpoint(id_filme_link):
    cursor = conn

    id = id_filme_link

    filme = buscar_filme.BuscarFilme(cursor, id)
    resultado = filme.buscar_filme()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_serie_nome/<nome_serie_link>", methods=["GET"])
def buscar_serie_endpoint(nome_serie_link):
    cursor = conn

    nome = nome_serie_link

    serie = buscar_serie.BuscarSerie(cursor, nome)
    resultado = serie.buscar_serie()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })


@app.route("/buscar_serie_id/<id_serie_link>", methods=["GET"])
def buscar_serie_endpoint(id_serie_link):
    cursor = conn

    id = id_serie_link

    serie = buscar_serie.BuscarSerie(cursor, id)
    resultado = serie.buscar_serie()
    cursor.close()
    return jsonify({
        "Titulo": resultado[1],
        "Ano": resultado[2],
        "Genero": resultado[3]
    })