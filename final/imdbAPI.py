# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# ESSE DAQUI GUARDA NO MOVIES E MOVIES HAS GENRE

from imdb import IMDb
import re
import urllib.request
import xml.etree.ElementTree as ET
import wptools
# Instead of pip install psycopg2 try pip install psycopg2-binary
import psycopg2
import psycopg2.extras

tabledef = [
    {
        "url": "movie",
        "format": ["person", "movieUri", "rating"],
        "table": "likesMovie"
    },
]

def xml2dict(tabledef):
    dict2ret = {}
    for tableitem in tabledef:
        itemList = []
        conn = urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/"+ tableitem["url"] + ".xml")
        xmltree = ET.parse(conn)
        root = xmltree.getroot()
        for item in root.iter():
            if item.attrib:
                itemObj = item.attrib
                elementList = []
                for attr in tableitem["format"]:
                    elementList.append(itemObj[attr])
                itemList.append(elementList)
        dict2ret[tableitem["table"]] = itemList
    return dict2ret

dictxml = xml2dict(tabledef)

list_movies = []

for key in dictxml.keys():
	for item in dictxml[key]:
			list_movies.append(item[1].split('/')[-2].split('t')[-1])

ia = IMDb()

# Try to connect
try:
    conn = psycopg2.connect("dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'")
except Exception as e:
    print(e)
    print("I am unable to connect to the database.")

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
      cur = conn.cursor()
      try:
        cur.execute(movies_query)
        for movie_has_genre_query in movie_has_genre_query_list:
          print(movie_has_genre_query)
          cur.execute(movie_has_genre_query)
      except Exception as e:
        print(e)
      conn.commit()