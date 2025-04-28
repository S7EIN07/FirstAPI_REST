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


@app.route("/buscar_filmes/", methods=["GET"])
def buscar_filmes():
    filme = buscar_filme.BuscarFilme()
    resultado = filme.buscar_filme()

    return jsonify({'resultado': resultado})


@app.route("/buscar_serie/", methods=["GET"])
def buscar_serie():
    serie = buscar_serie.BuscarSerie()
    resultado = serie.buscar_serie()
    
    return jsonify({'resultado': resultado})