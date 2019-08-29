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

# read json files
READ = {"bands":False, "band_has_genre":False, "likes_band":True,
    "movies":True, "movie_has_genre":True, "likes_movie":True} 

# extract information from files
EXTRACT = {"bands":True, "band_has_genre":True, "likes_band":False,
    "movies":False, "movie_has_genre":False, "likes_movie":False} # read json files

# write json files
WRITE = {"bands":True, "band_has_genre":True, "likes_band":False,
    "movies":True, "movie_has_genre":True, "likes_movie":True} # read json files

# send tables to db
SAVE = {"bands":True, "band_has_genre":True, "likes_band":True,
    "movies":True, "movie_has_genre":True, "likes_movie":True} # read json files


tables = {"bands":[], "band_has_genre":[], "likes_band":[],
    "movies":[], "movie_has_genre":[], "likes_movie":[]}
tables_path = {"bands": "./tables_json/bands.json",
    "band_has_genre":   "./tables_json/band_has_genre.json",
    "likes_band":       "./tables_json/likes_band.json",
    "movies":           "./tables_json/movies.json", 
    "movie_has_genre":  "./tables_json/movie_has_genre.json", 
    "likes_movie":      "./tables_json/likes_movie.json"}


print("Initialize files reading...")
for table in tables_path:
    if(READ[table]):
        try:
            with open(tables_path[table]) as f:
                tables[table] = json.loads(f.read())
        except Exception as e:
            print(e)
print("Finished file reading!")

if EXTRACT:
    print("Initialize information extraction...")
    # Bands table
    if(EXTRACT["bands"]):
        print("Initializing Wikipedia extraction...")
        tables["bands"] = generateWikipediaTuples()
        print("Finished Wikipedia extraction!")

    # Bands related tables
    if(EXTRACT["bands"] and EXTRACT["band_has_genre"]):
        print("Initializing Spotify extraction...")
        updateBandsInfo(tables["bands"], tables["band_has_genre"])
        print("Finished Spotify extraction!")

    # Movies related tables
    if(EXTRACT["movies"] and EXTRACT["movie_has_genre"]):
        print("Initializing IMDb extraction...")
        movie_related_tables = generateIMDbTuples()
        tables["movies"], tables["movie_has_genre"] = \
            movie_related_tables["movies"], movie_related_tables["movie_has_genre"]
        print("Finished IMDb!")

    # Users likes tables
    if(EXTRACT["likes_band"] and EXTRACT["likes_movie"]):
        print("Initializing likes XML extraction...")
        user_related_tables = generateLikesTuples()
        tables["likes_band"], tables["likes_movie"] = \
            user_related_tables["likes_band"], user_related_tables["likes_movie"]
        print("Finished likes XML extraction!")
        print("Finished information extraction!")


print("Initialize file writing...")
for table in tables_path:
    if(WRITE[table]):
        try:
            with open(tables_path[table], 'w') as f:
                f.write(json.dumps(tables[table])) 
        except Exception as e:
            print(e)
print("Finished file writing!")

if SAVE:
    print("Initialize DB saving...")
    if(SAVE["bands"]):
        send2db(tables["bands"], "bands")
    if(SAVE["band_has_genre"]):
        send2db(tables["band_has_genre"], "band_has_genre")
    if(SAVE["likes_band"]):
        send2db(tables["likes_band"], "likes_band")
    if(SAVE["movies"]):
        send2db(tables["movies"], "movies")
    if(SAVE["movie_has_genre"]):
        send2db(tables["movie_has_genre"], "movie_has_genre")
    if(SAVE["likes_movie"]):
        send2db(tables["likes_movie"], "likes_movie")
    print("Finished DB saving!")