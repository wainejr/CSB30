# source bin/activate

from flask import Flask
from flask_cors import CORS
from flask import jsonify
from band_genre_handler import *
from movie_handler import *
from user_handler import *
from bands_handler import *

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
        data.append(lista[1])

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


# retorna todos a quantidade de likes e o rating medio dos filmes de cada ano
# formato de objeto: 
# {
#   "labels": [2002, 2003],
#     "data": {
#         "data_1": [4, 5], # rating medio
#         "data_2": [13, 17], # quantidade de likes
#     }
# }
@app.route("/3_data/likes_per_year_and_rating")
def likes_per_year():
    labels = []
    data = {
        "data_1": [],
        "data_2": [],
    }

    for lista in get_movies_likes_by_date():
        labels.append(lista[0])
        data["data_1"].append(lista[1])
        data["data_2"].append(lista[2])

    return jsonify({
        "labels": labels,
        "data": data
    })


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

if __name__ == "__main__":
    app.run(debug=True)
