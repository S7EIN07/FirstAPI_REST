from flask import Flask, jsonify
import psycopg
import os
from dotenv import load_dotenv
from codes import (
    buscar_filme_nome, buscar_filme_id, buscar_omdb_filme_id, 
    buscar_omdb_filme_nome, buscar_serie_nome, buscar_serie_id, 
    buscar_omdb_serie_id, buscar_omdb_serie_nome, inserir_filme,
    inserir_serie, mostrar_dados
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


mostrar_dados_instance = mostrar_dados.MostrarDados(conn, API_KEY)


@app.route("/filme/nome/<nome>", methods=["GET"])
def buscar_filmes_endpoint_nome(nome):
    return mostrar_dados_instance.buscar_item(
        tipo = "filme",
        identificador = "nome",
        valor = nome,
        buscar_local_func = lambda conn, val: buscar_filme_nome.BuscarFilmeNome(conn, val).buscar_filme_nome,
        buscar_omdb_func = lambda conn, val, key: buscar_omdb_filme_nome.BuscarOMDbFilmeNome(conn, val, key).buscar_omdb_filme_nome,
        inserir_fun = inserir_filme.InserirFilme
    )


@app.route("/filme/id/<id>", methods=["GET"])
def buscar_filmes_endpoint_id(id):
   return mostrar_dados_instance.buscar_item(
        tipo = "filme",
        identificador = "id",
        valor = id,
        buscar_local_func = lambda conn, val: buscar_filme_id.BuscarFilmeId(conn, val).buscar_filme_id,
        buscar_omdb_func = lambda conn, val, key: buscar_omdb_filme_id.BuscarOMDbFilmeId(conn, val, key).buscar_omdb_filme_id,
        inserir_fun = inserir_filme.InserirFilme
    )


@app.route("/serie/nome/<nome>", methods=["GET"])
def buscar_serie_endpoint_nome(nome):
     return mostrar_dados_instance.buscar_item(
        tipo = "serie",
        identificador = "nome",
        valor = nome,
        buscar_local_func = lambda conn, val: buscar_serie_nome.BuscarSerieNome(conn, val).buscar_serie_nome,
        buscar_omdb_func = lambda conn, val, key: buscar_omdb_serie_nome.BuscarOMDbSerieNome(conn, val, key).buscar_omdb_serie_nome,
        inserir_fun = inserir_serie.InserirSerie
    )


@app.route("/serie/id/<id>", methods=["GET"])
def buscar_serie_endpoint_id(id):
   return mostrar_dados_instance.buscar_item(
        tipo = "serie",
        identificador = "id",
        valor = id,
        buscar_local_func = lambda conn, val: buscar_serie_id.BuscarSerieId(conn, val).buscar_serie_id,
        buscar_omdb_func = lambda conn, val, key: buscar_omdb_serie_id.BuscarOMDbSerieId(conn, val, key).buscar_omdb_serie_id,
        inserir_fun = inserir_serie.InserirSerie
    )