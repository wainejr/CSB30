# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imdb import IMDb
from xml2dict import xml2dict

def generateIMDbTuples():
    movies_ids = []
    movie_related_tuples = {"movies": [], "movie_has_genre": []}
    seen_movies = set()

    movie_dict = xml2dict("movie")

    for key in movie_dict.keys():
        for item in movie_dict[key]:
            movies_ids.append(item[1].split("/")[-2].split("t")[-1])

    ia = IMDb()

    for movie_id in movies_ids:
        if movie_id not in seen_movies:
            seen_movies.add(movie_id)

            imdbmovie = ia.get_movie(movie_id)

            months = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12",
            }

            date_formated = (
                imdbmovie["original air date"].split()[2]
                + "-"
                + months[imdbmovie["original air date"].split()[1]]
                + "-"
                + imdbmovie["original air date"].split()[0]
            )

            movie_related_tuples["movies"].append(
                {
                    "values": [
                        "http://www.imdb.com/title/tt" + movie_id + "/",
                        str(imdbmovie["canonical title"]).replace("'", ""),
                        date_formated,
                        str(imdbmovie["directors"][0]).replace("'", ""),
                        int(float(imdbmovie["rating"])*10)
                    ]
                }
            )
            print(movie_related_tuples["movies"][-1])

            for genre in imdbmovie["genres"]:
                movie_related_tuples["movie_has_genre"].append(
                    {
                        "values": [
                            "http://www.imdb.com/title/tt" + movie_id + "/",
                            str(genre).replace("'", ""),
                        ]
                    }
                )
                print(movie_related_tuples["movie_has_genre"][-1])

    return movie_related_tuples
