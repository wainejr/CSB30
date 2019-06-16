# source bin/activate

from flask import Flask
from flask import jsonify
from supergenre_handler import *
		
app = Flask(__name__)

@app.route('/chart/all_genres')
def index():
    return jsonify(get_all_genres())

@app.route('/chart/count_supergenres')
def count_supergenres():
    labels = []
    data = []

    for lista in get_count_bands_in_supergenres():
        labels.append(lista[0])
        data.append(lista[1])

    return jsonify({"labels": labels, "data": data})

if __name__ == '__main__':
    app.run(debug=True)