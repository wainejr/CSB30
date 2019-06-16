from postgree import *


def get_most_popular_bands():
    query_cmd = "SELECT B.artistic_name, COUNT(*) AS Total\
        FROM likes_band LB, bands B \
        WHERE LB.id_band = B.id\
        GROUP BY B.artistic_name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)
