from postgree import *


def get_most_popular_users():
    query_cmd = "SELECT U.name, COUNT(*) AS Total\
        FROM friends F, users U \
        WHERE F.id_user_2 = U.id\
        GROUP BY U.name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


def get_most_popular_cities():
    query_cmd = "SELECT Lower(U.hometown), COUNT(*) AS Total\
        FROM users U \
        GROUP BY Lower(U.hometown) \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)
