# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# ESSE DAQUI GUARDA NO MOVIES E MOVIES HAS GENRE

from imdb import IMDb
from xml2dict import xml2dict
from postgree import connect

movie_dict = xml2dict("movie")

list_movies = []

for key in movie_dict.keys():
	for item in movie_dict[key]:
			list_movies.append(item[1].split('/')[-2].split('t')[-1])

ia = IMDb()

conn = connect()

seen_movie = set()

for movie in list_movies:
    imdbmovie = ia.get_movie(movie)
    months = {
      'Jan': '01',
      'Feb': '02',
      'Mar': '03',
      'Apr': '04',
      'May': '05',
      'Jun': '06',
      'Jul': '07',
      'Aug': '08',
      'Sep': '09',
      'Oct': '10',
      'Nov': '11',
      'Dec': '12'
    }
    date_formated = imdbmovie['original air date'].split()[2] + "-" + months[imdbmovie['original air date'].split()[1]] + "-" + imdbmovie['original air date'].split()[0]

    movies_query = "INSERT INTO movies VALUES ('http://www.imdb.com/title/tt{}/', '{}', '{}', '{}')".format(
      movie, 
      str(imdbmovie['canonical title']).replace("'", ""),
      date_formated,
      str(imdbmovie['directors'][0]).replace("'", ""))

    movie_has_genre_query_list = []

    for genre in imdbmovie['genres']:
      movie_has_genre_query_list.append("INSERT INTO movie_has_genre VALUES ('http://www.imdb.com/title/tt{}/', '{}')".format(
        movie,
        str(genre).replace("'", "")
      ))

    if movies_query not in seen_movie:
      print(movies_query)
      seen_movie.add(movies_query)
      # cursor = conn.cursor()
      try:
        # cursor.execute(movies_query)
        for movie_has_genre_query in movie_has_genre_query_list:
          print(movie_has_genre_query)
          # cursor.execute(movie_has_genre_query)
      except Exception as e:
        print(e)
      # conn.commit()