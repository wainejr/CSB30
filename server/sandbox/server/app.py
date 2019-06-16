from flask import Flask
from flask import jsonify
from supergenre_handler import *
		
app = Flask(__name__)

@app.route('/all_genres')
def index():
    return jsonify({"genres": get_all_genres()})

@app.route('/all_genres')
def index():
    return jsonify({"genres": get_all_genres()})

if __name__ == '__main__':
    app.run(debug=True)