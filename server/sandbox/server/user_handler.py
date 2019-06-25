from postgree import *


def get_most_popular_users():
    query_cmd = "SELECT U.name, COUNT(*) AS Total\
        FROM friends F, users U \
        WHERE F.id_user_2 = U.id\
        GROUP BY U.name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


def get_name_id():
    query_cmd = "SELECT U.id, U.name\
        FROM users U;"

    return fetch_from_query(query_cmd)


def get_most_popular_cities():
    query_cmd = "SELECT Lower(U.hometown), COUNT(*) AS Total\
        FROM users U \
        GROUP BY Lower(U.hometown) \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


def get_common_friends(user_id_1, user_id_2):
    query_cmd = "SELECT U.name\
        FROM users U, friends F1, friends F2\
        WHERE '{}' = F1.id_user_1 AND '{}' = F2.id_user_1 AND \
        F1.id_user_2 = F2.id_user_2 AND U.id = F1.id_user_2 \
        ORDER BY U.name;".format(user_id_1, user_id_2)

    return fetch_from_query(query_cmd)

