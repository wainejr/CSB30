# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imdb_api import generateIMDbTuples
from wikipedia_api import generateWikipediaTuples
from user_likes import generateLikesTuples
from spotify_api import updateBandsInfo
from postgree import send2db
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
tuples = {"bands":[], "band_has_genre":[], "likes_band":[],
    "movies":[], "movie_has_genre":[], "likes_movie":[]}

try:
    with open('tuples.txt') as f:
        tuples = json.loads(f.read())
except Exception as e:
    print(e)

tuples.update(generateWikipediaTuples())
pp.pprint("Finished Wikipedia!")
updateBandsInfo(tuples["bands"], tuples["band_has_genre"])
tuples.update(tuples)
pp.pprint("Finished Spotify!")
tuples.update(generateIMDbTuples())
pp.pprint("Finished IMDb!")
tuples.update(generateLikesTuples())
pp.pprint("Finished likes XML!")

with open('tuples.txt', 'w') as file:
    file.write(json.dumps(tuples)) 
    # use `json.loads` to do the reverse
