# API REST de Busca de Filmes e Séries

Esta é a documentação para a API REST de busca de filmes e séries. Esta API permite que os usuários pesquisem informações sobre filmes e séries, buscando em um banco de dados local e, caso não encontre, consultando a API OMDb. Os resultados da OMDb são então armazenados no banco de dados local para buscas futuras.

## Clonando o Projeto

Para obter o código-fonte desta API REST, você pode cloná-lo diretamente do GitHub utilizando o comando:

```bash
git clone https://github.com/S7EIN07/FirstAPI_REST.git
```

Após entre na pasta:

```bash
cd FirstAPI_REST
```

# Ambiente Virtual com venv (Python)

Este projeto recomenda o uso de um **ambiente virtual** para isolar as dependências e evitar conflitos com outras bibliotecas instaladas no seu sistema.

## O que é o `venv`?

O `venv` é um módulo do Python que permite criar ambientes virtuais — diretórios que contêm uma instalação independente do Python e das bibliotecas necessárias para um projeto. Ele ajuda a manter seu projeto limpo, organizado e compatível com outros sistemas.

## Como criar e ativar um ambiente virtual

### 1. Criar o ambiente virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv .venv
```
### Ativar o ambiente virtual
No Windows:
```bash
.venv\Scripts\activate
```
No Linux ou macOS:
```bash
source .venv/bin/activate
```

## Bibliotecas Utilizadas

Este projeto utiliza as bibliotecas Python que estão abaixo, ultilize o comando pip para efetuar a instalação das bibliotecas:

```python
pip install flask psycopg[binary] python-dotenv requests
```


* **Flask**: Um microframework web para construir a API REST.
    ```python
    from flask import Flask, jsonify
    ```
    <sup>jsonify é uma das funções do flask usada para transformar em json<sup>

* **psycopg**: Um adaptador PostgreSQL para Python, usado para interagir com o banco de dados.
    ```python
    import psycopg
    ```

* **python-dotenv**: Usado para carregar variáveis de ambiente de um arquivo `.env`.
    ```python
    from dotenv import load_dotenv
    ```
  <sup>No nosso projeto foi usado apenas a função load_dotenv<sup>


* **requests**: Usado dentro dos módulos `codes.buscar_omdb_filme_nome`, `codes.buscar_omdb_filme_id`, `codes.buscar_omdb_serie_nome` e `codes.buscar_omdb_serie_id` para fazer requisições à API OMDb.
    ```python
    import requests
    ```

## Estrutura de Código (Módulos `codes`)

O código está organizado em módulos dentro de um diretório `codes/`, que contêm as seguintes classes e funcionalidades:

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

**Endpoint:** `/filme/nome/<nome>`

**Método:** `GET`

**Descrição:** Busca informações de um filme pelo nome. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `nome` (string, obrigatório): O nome do filme a ser buscado.

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000/filme/nome/Ultimato
```
**Este exemplo de requisição retorna:**
```json
{
    {
        "Ano": "2004",
        "Classificação Indicativa": "N/A",
        "Duração": "12 min",
        "Genero": "Short, Drama",
        "Lingua(s)": "Portuguese",
        "Pais(es)": "Portugal",
        "Plot": "N/A",
        "Tipo": "movie",
        "Titulo": "Ultimato",
        "msg": "Buscado na OMDB e postado no BD"
    },
}
```
### 2. Buscar Filme por ID (OMDb ID)

**Endpoint:** `/filme/id/<id>`

**Método:** `GET`

**Descrição:** Busca informações de um filme pelo ID OMDb. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `id` (string, obrigatório): O ID OMDb do filme a ser buscado (ex: `tt0367279`).

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000/filme/id/tt1746625
```
**Este exemplo de requisição retorna:**
```json
{
    "Ano": 2004,
    "Classificação Indicativa": "N/A",
    "Duração": "12 min",
    "Genero": "Short, Drama",
    "Lingua(s)": "Portuguese",
    "Pais(es)": "Portugal",
    "Plot": "N/A",
    "Série ou Filme": "movie",
    "Titulo": "Ultimato",
    "msg": "Busca no DB"
}
```
### 3. Buscar Série por Nome

**Endpoint:** `/serie/nome/<nome>`

**Método:** `GET`

**Descrição:** Busca informações de uma série pelo nome. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `nome` (string, obrigatório): O nome da série a ser buscada.

**Exemplo de Requisição:**

```http
GET http://127.0.0.1:5000/serie/nome/Breaking Bad
```

**Este exemplo de requisição retorna:**

```json
{
   "Ano": "2008–2013",
    "Classificação Indicativa": "TV-MA",
    "Duração": "49 min",
    "Genero": "Crime, Drama, Thriller",
    "Lingua(s)": "English, Spanish",
    "Pais(es)": "United States",
    "Plot": "A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student to secure his family's future.",
    "Temporadas": null,
    "Tipo": "series",
    "Titulo": "Breaking Bad",
    "msg": "Buscado na OMDB e postado no BD"
},

```
### 4. Buscar Série por ID (OMDb ID)

**Endpoint:** `/serie/id/<id>`

**Método:** `GET`

**Descrição:** Busca informações de uma série pelo ID OMDb. Primeiro, tenta encontrar no banco de dados local. Se não encontrar, consulta a API OMDb e armazena o resultado no banco de dados antes de retornar.

**Parâmetros de Caminho:**

* `id` (string, obrigatório): O ID OMDb da serie a ser buscado (ex: `tt0118421`).

**Exemplo de Requisição:**
```http
GET http://127.0.0.1:5000/serie/id/tt0118421
```
**Este exemplo de requisição retorna:**
```json
{
    "Ano": "1997–2003",
    "Classificação Indicativa": "TV-MA",
    "Duração": "31S min",
    "Genero": "Crime, Drama, Thriller",
    "Lingua(s)": "English",
    "Pais(es)": "United States",
    "Plot": "A series chronicling the daily activities of an unusual prison facility and its criminal inhabitants.",
    "Série ou Filme": "series",
    "Temporadas": null,
    "Titulo": "Oz",
    "msg": "Buscado na OMDB e postado no BD"
}
```
