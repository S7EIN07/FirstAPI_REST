# API REST de Busca de Filmes e Séries

Esta é a documentação para a API REST de busca de filmes e séries. Esta API permite que os usuários pesquisem informações sobre filmes e séries, buscando em um banco de dados local e, caso não encontre, consultando a API OMDb. Os resultados da OMDb são então armazenados no banco de dados local para buscas futuras.

## Bibliotecas Utilizadas

Este projeto utiliza as seguintes bibliotecas Python:

* **Flask**: Um microframework web para construir a API REST.
    ```python
    from flask import Flask, jsonify
    ```

* **psycopg**: Um adaptador PostgreSQL para Python, usado para interagir com o banco de dados.
    ```python
    import psycopg
    ```

* **python-dotenv**: Usado para carregar variáveis de ambiente de um arquivo `.env`.
    ```python
    from dotenv import load_dotenv
    ```

* **requests**: Usado dentro dos módulos `codes.buscar_omdb_filme_nome`, `codes.buscar_omdb_filme_id`, `codes.buscar_omdb_serie_nome` e `codes.buscar_omdb_serie_id` para fazer requisições à API OMDb).
    ```python
    # Exemplo de uso (provável dentro dos módulos 'codes')
    import requests
    ```

## Estrutura de Código (Módulos `codes`)

O código está organizado em módulos dentro de um diretório `codes/` (a estrutura exata pode variar), que contêm as seguintes classes e funcionalidades:

* **`buscar_filme_nome.py`**: Contém a classe `BuscarFilmeNome` para buscar filmes por nome no banco de dados local.
* **`buscar_filme_id.py`**: Contém a classe `BuscarFilmeId` para buscar filmes por ID no banco de dados local.
* **`buscar_omdb_filme_nome.py`**: Contém a classe `BuscarOMDbFilmeNome` para buscar informações de filmes por nome na API OMDb.
* **`buscar_omdb_filme_id.py`**: Contém a classe `BuscarOMDbFilmeId` para buscar informações de filmes por ID na API OMDb.
* **`buscar_serie_nome.py`**: Contém a classe `BuscarSerieNome` para buscar séries por nome no banco de dados local.
* **`buscar_serie_id.py`**: Contém a classe `BuscarSerieId` para buscar séries por ID no banco de dados local.
* **`buscar_omdb_serie_id.py`**: Contém a classe `BuscarOMDbSerieId` para buscar informações de séries por ID na API OMDb.
* **`buscar_omdb_serie_nome.py`**: Contém a classe `BuscarOMDbSerieNome` para buscar informações de séries por nome na API OMDb.
* **`inserir_filme.py`**: Contém a classe `InserirFilme` para inserir dados de filmes no banco de dados local.
* **`inserir_serie.py`**: Contém a classe `InserirSerie` para inserir dados de séries no banco de dados local.

## Configuração de Variáveis de Ambiente

As seguintes variáveis de ambiente são necessárias e devem ser configuradas em um arquivo `.env`:
* **`API_KEY=<sua_chave_omdb>`**
* **`DB_NAME=<nome_do_seu_banco_de_dados>`**
* **`DB_USER=<nome_do_usuario_do_banco>`**
* **`DB_PASSWORD=<senha_do_banco>`**
* **`DB_HOST=<host_do_banco>`**
* **`DB_PORT=<porta_do_banco>`**

## Endpoints

### 1. Buscar Filme por Nome

**Endpoint:** `/buscar_filme_nome/<nome_filme_link>`

**Método:** `GET`

**Descrição:** Busca informações de um filme pelo nome. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `nome_filme_link` (string, obrigatório): O nome do filme a ser buscado.

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000//buscar_filme_nome/Ultimato
```
**Este exemplo de requisição retorna:**
```json
{
    "Ano": "2004",
    "Filme ou Série": "Filme",
    "Genero": "Short, Drama",
    "Titulo": "Ultimato",
}
```
### 2. Buscar Filme por ID (IMDb ID)

**Endpoint:** `/buscar_filme_id/<id_filme_link>`

**Método:** `GET`

**Descrição:** Busca informações de um filme pelo ID IMDb. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `id_filme_link` (string, obrigatório): O ID IMDb do filme a ser buscado (ex: `tt0367279`).

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000//buscar_filme_id/tt1746625
```
**Este exemplo de requisição retorna:**
```json
{
    "Ano": "2004",
    "Filme ou Série": "Filme",
    "Genero": "Short, Drama",
    "Titulo": "Ultimato",
}
```
### 3. Buscar Série por Nome

**Endpoint:** `/buscar_serie_nome/<nome_serie_link>`

**Método:** `GET`

**Descrição:** Busca informações de uma série pelo nome. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `nome_serie_link` (string, obrigatório): O nome da série a ser buscada.

**Exemplo de Requisição:**

```http
GET http://127.0.0.1:5000/buscar_serie_nome/Breaking Bad
```

**Este exemplo de requisição retorna:**

```json
{
    "Ano": "2008–2013",
    "Filme ou Série": "series",
    "Genero": "Crime, Drama, Thriller",
    "Titulo": "Breaking Bad",
}
```
### 4. Buscar Série por ID (IMDb ID)

**Endpoint:** `/buscar_serie_id/<id_serie_link>`

**Método:** `GET`

**Descrição:** Busca informações de uma série pelo ID IMDb. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `id_serie_link` (string, obrigatório): O ID IMDb da serie a ser buscado (ex: `tt0118421`).

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000//buscar_serie_id/tt0118421
```
**Este exemplo de requisição retorna:**
```json
{
    "Ano": "1997–2003",
    "Filme ou Série": "Série",
    "Genero": "Crime, Drama, Thriller",
    "Titulo": "Oz",
}
```