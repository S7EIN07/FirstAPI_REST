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


@app.route("/buscar_filme/", methods=["GET"])
def buscar_filmes_endpoint():
    cursor = conn
    filme = buscar_filme.BuscarFilme(cursor)
    resultado = filme.buscar_filme()
    cursor.close()
    return jsonify({'resultado': resultado})


@app.route("/buscar_serie/", methods=["GET"])
def buscar_serie_endpoint():
    cursor = conn
    serie = buscar_serie.BuscarSerie(cursor)
    resultado = serie.buscar_serie()
    cursor.close()
    return jsonify({'resultado': resultado})