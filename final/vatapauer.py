# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imdbAPI import generateIMDbTuples
from wikipediaAPI import generateWikipediaTuples
from user_likes_shit import generateLikesTuples
from spotifyAPI import getBandGenre

tuples = {}

tuples.update(generateIMDbTuples())
tuples.update(generateWikipediaTuples())
tuples.update(generateLikesTuples())
