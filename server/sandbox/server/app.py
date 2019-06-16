# source bin/activate

from flask import Flask
from flask import jsonify
from band_genre_handler import *
from movie_handler import *
from user_handler import *
from bands_handler import *

app = Flask(__name__)


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


@app.route("/genres")
def genres():
    return jsonify({"genres": get_all_genres()})


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

    for lista in get_most_popular_movies():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


@app.route("/chart/top_bands")
@app.route("/chart/top_bands/<quant>")
def top_bands(quant=None):
    labels = []
    data = []

    for lista in get_most_popular_bands():
        labels.append(lista[0])
        data.append(lista[1])

    return prepare_chart_json(quant, labels, data)


if __name__ == "__main__":
    app.run(debug=True)
