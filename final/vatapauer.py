# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imdb_api import generateIMDbTuples
from wikipedia_api import generateWikipediaTuples
from user_likes_shit import generateLikesTuples
from spotify_api import generateBandGenresTuples
import json

tuples = {}

tuples.update(generateWikipediaTuples())
tuples.update(generateBandGenresTuples(tuples))
tuples.update(generateIMDbTuples())
tuples.update(generateLikesTuples())

print(tuples)

with open('tuples.txt', 'w') as file:
    file.write(json.dumps(tuples)) # use `json.loads` to do the reverse
