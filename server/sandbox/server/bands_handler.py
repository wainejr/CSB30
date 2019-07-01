from postgree import *


def get_most_liked_bands():
    query_cmd = "SELECT B.artistic_name, COUNT(*) AS Total\
        FROM likes_band LB, bands B \
        WHERE LB.id_band = B.id\
        GROUP BY B.artistic_name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


def get_most_followed_bands():
    query_cmd = "SELECT B.artistic_name AS Nome, c as Followers, \
            B.popularity AS Popularidade\
        FROM bands B \
        WHERE B.followers > 0 \
        ORDER BY Followers DESC;"

    return fetch_from_query(query_cmd)


def get_most_popular_bands():
    query_cmd = "SELECT B.artistic_name, B.followers as Followers, COUNT(*) AS Likes \
        FROM likes_band LB, bands B \
        WHERE LB.id_band = B.id AND B.followers > 0\
        GROUP BY B.artistic_name, Followers \
        ORDER BY Likes DESC, Followers DESC;"

    return fetch_from_query(query_cmd)

def get_likes_bands():
    query_cmd = "SELECT B.artistic_name, AVG(LB.rating) AS Rating, COUNT(*) AS Total\
        FROM likes_band LB, bands B \
        WHERE LB.id_band = B.id \
        GROUP BY B.artistic_name \
        ORDER BY Rating DESC;"
    return fetch_from_query(query_cmd)
