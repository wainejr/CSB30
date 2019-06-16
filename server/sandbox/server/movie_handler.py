from postgree import *


def get_most_popular_movies():
    query_cmd = "SELECT M.title, COUNT(*) AS Total\
        FROM likes_movie LM, movies M \
        WHERE LM.id_movie = M.id\
        GROUP BY M.title \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)
