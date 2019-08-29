# source bin/activate

from flask import Flask
from flask_cors import CORS
from flask import jsonify
from band_genre_handler import *
from movie_handler import *
from user_handler import *
from bands_handler import *
from collections import defaultdict

app = Flask(__name__)
cors = CORS(app)



# ------------------------------------------------------------ #
# Funcoes Auxiliares #
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def prepare_chart_json(quant, labels, data):
    if not quant:
        quant = len(labels)
    return jsonify(
        {
            "labels": labels[0 : clamp(int(quant), 0, len(labels) - 1)],
            "data": data[0 : clamp(int(quant), 0, len(data) - 1)],
        }
    )
# ------------------------------------------------------------ #

# formato objeto:
# {
#   "genres": [
#     [
#       "acid jazz",    # nome
#       1               # quantidade
#     ], 
#   ]
# }
@app.route("/genres")
def genres():
    return jsonify({"genres": get_all_genres()})


# ------------------------------------------------------------ #
# Rotas de chart 
# formato objeto: 
# {
#   "labels": [],
#   "data": []
# }
@app.route("/chart/count_supergenres")
@app.route("/chart/count_supergenres/<quant>")
def count_supergenres(quant=None):
    labels = []
    data = []

    for lista in get_count_bands_in_supergenres():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/count_genres_in_supergenres")
@app.route("/chart/count_genres_in_supergenres/<quant>")
def genres_in_supergenres(quant=None):
    labels = []
    data = []

    for lista in get_count_genres_in_supergenres():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/most_popular_users")
@app.route("/chart/most_popular_users/<quant>")
def most_popular_users(quant=None):
    labels = []
    data = []

    for lista in get_most_popular_users():
        nome = lista[0].split()[0] + " "
        if lista[0].split()[1].lower() == "de" or lista[0].split()[1].lower() == "da":
            nome += lista[0].split()[2]
            print(lista[0].split()[1].lower())
            print(lista[0].split()[2])
        else:
            nome += lista[0].split()[1]

        labels.append(nome)
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/top_cities")
@app.route("/chart/top_cities/<quant>")
def top_x_cities(quant=None):
    labels = []
    data = []

    for lista in get_most_popular_cities():
        if lista[0] != "":
            labels.append(lista[0].title())
            data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/top_movies")
@app.route("/chart/top_movies/<quant>")
def top_movies(quant=None):
    labels = []
    data = []

    for lista in get_most_liked_movies():
        labels.append(lista[0])
        data.append(round(float(lista[1]), 2))

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/top_bands")
@app.route("/chart/top_bands/<quant>")
def top_bands(quant=None):
    labels = []
    data = []

    for lista in get_most_liked_bands():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/bands_rating")
@app.route("/chart/top_bands/<quant>")
def bands_rating(quant=None):
    labels = []
    data = []

    for band in get_likes_bands():
        labels.append(str(band[0]))
        data.append(round(float(band[1]), 2))

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/followers_by_band")
@app.route("/chart/followers_by_band/<quant>")
def followers_by_band(quant=None):
    labels = []
    data = []

    for lista in get_most_popular_bands():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)

# ------------------------------------------------------------ #


# ------------------------------------------------------------ #
# Rotas sem padronizacao de retorno #

# returns all users
# formato objeto: 
# {
#   "users": [
#       {
#         "id": "http://utfpr.edu.br/CSB30/2019/1/DI1901giovanniforastieri",
#         "name": "Giovanni Forastieri"
#       },
#   ]
# }
@app.route("/users")
def all_users():
    obj = {
        "users": []
    }
    for user in get_all_users_name_and_id():
        obj["users"].append({
            "id": user[0],
            "name": user[1]
        })

    return jsonify(obj)


# user example: http://utfpr.edu.br/CSB30/2019/1/DI1901giovanniforastieri
# formato objeto:
# {
#   "distancias": [
#     {
#       "nome": "Ian Douglas",
#       "distancia": 0
#     }
#   ],
# }
@app.route("/relationship_level/<path:user_id>")
def lvl(user_id):

    retorno = {
        "distancias": [],
    }
    for distancia in get_realtionship_lvl(user_id):
        retorno["distancias"].append({
            "nome": distancia[0],
            "distancia": distancia[1]
        })
    return jsonify(retorno)


# retorna todos a quantidade de likes dos filmes de cada ano
# formato de objeto: 
# {
#   "2000s": 65, 
#   "2010s": 61, 
#   "30s": 1, 
#   "50s": 1, 
#   "60s": 6, 
#   "70s": 24, 
#   "80s": 23, 
#   "90s": 68
# }
@app.route("/most_popular_decades")
def decades():
    decadas = defaultdict(int)
    
    for ano in get_movies_likes_by_date():
        if str(int(ano[0]/10))[:-1] == "19":
            decadas[str(int(ano[0]/10))[-1] + "0s"] += ano[2]
        else:
            decadas[str(int(ano[0]/10)) + "0s"] += ano[2]

    return jsonify(decadas)


# ------------------------------------------------------------ #


# ------------------------------------------------------------ #
# Rotas formato de lista #

# separar usando &&
# exemplo: http://utfpr.edu.br/CSB30/2019/1/DI1901giovanniforastieri&&http://utfpr.edu.br/CSB30/2019/1/DI1901ianqueros
# retorna todos as bandas em dois generos
# formato de lista ex: ["Alan", "Bruna"]
@app.route("/list/common_friends/<path:users>")
def common_friends(users):
    friends = get_common_friends(users.split("&&")[0], users.split("&&")[1])
    retorno = []
    for user in friends:
        retorno.append(user[0])
    return jsonify(retorno)


# separar usando &&
# exemplo: Pop&&Rock
# retorna todos as bandas em dois generos
# formato de lista ex: ["Red Hot", "Strokes"]
@app.route("/list/bands_in_both_genres/<path:genres>")
def bands_in_both_genres(genres):
    genres_related = get_genres_intersection(genres.split("&&")[0], genres.split("&&")[1])
    retorno = []
    for genre in genres_related:
        retorno.append(genre[0])
    return jsonify(retorno)


# separar usando &&
# exemplo: Pop&&Rock
# retorna todos as bandas em dois generos
# formato de lista ex: ["Red Hot", "Strokes"]
@app.route("/list/genres")
def all_genres():
    retorno = []
    for genre in get_all_genres():
        retorno.append(genre[0])
    return jsonify(retorno)


# separar usando &&
# exemplo: Pop&&Rock
# retorna todos as bandas em dois supergeneros
# formato de lista ex: ["Red Hot", "Strokes"]
@app.route("/list/bands_in_both_supergenres/<path:genres>")
def bands_in_both_supergenres(genres):
    genres_related = get_supergenres_intersection(genres.split("&&")[0], genres.split("&&")[1])
    retorno = []
    for genre in genres_related:
        retorno.append(genre[0])
    return jsonify(retorno)


# retorna todos os nomes dos generos dos filmes de cada diretor
# formato de lista ex: ["Acao", "Aventura"]
@app.route("/list/director_genres/<path:director_name>")
def director_genres(director_name):
    genres = []

    for genre in get_director_genres(director_name):
        genres.append(genre[0])

    return jsonify(genres)


# retorna todos os Nomes dos diretores
# formato de lista ex: ["Quentin Tarantino", "Sla quem das contas"]
@app.route("/list/directors")
def all_directors():
    directors = []

    for director in get_all_directors():
        directors.append(director[0])

    return jsonify(directors)


# retorna todos os nomes dos filmes
# formato de lista ex: ["Inception", "Piratas do caribe"]
@app.route("/list/movies")
def all_movies():
    movies = []

    print(get_all_movies())
    for movie in get_all_movies():
        movies.append(movie[0].split(",")[0])

    return jsonify(movies)   


# retorna todos os nomes das bandas
# formato de lista ex: ["Strokes", "Red Hot"]
@app.route("/list/bands")
def all_bands():
    bands = []

    for band in get_all_bands():
        bands.append(band[0])

    return jsonify(bands)    


if __name__ == "__main__":
    app.run(debug=True)
