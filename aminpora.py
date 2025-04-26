from flask import Flask, request, jsonnify
import psycopg
from codes import buscar

app = Flask(__name__)

@app.route("/buscar_filmes/", methods=["GET"])
def buscar_filmes():
    buscar.BuscarFilme.buscar_filme()
    return

@app.route("/buscar_serie/", methods=["GET"])
def buscar_serie():
    buscar.BuscarSerie.buscar_serie()
    return
