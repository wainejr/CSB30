from postgree import *

def get_most_popular_users():
    query_cmd = "SELECT U.name, COUNT(*) AS Total\
        FROM friends F, users U \
        WHERE F.id_user_2 = U.id\
        GROUP BY U.name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


def get_all_users_name_and_id():
    query_cmd = "SELECT U.id, U.name\
        FROM users U \
        ORDER BY U.name;"

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


# return level of relationship from one person to all others
def get_realtionship_lvl(user_id):
    query_cmd = "WITH RECURSIVE Conhece AS\
        (\
            SELECT id_user_2 AS id2, 0 AS nivel\
            FROM Friends\
            WHERE id_user_1 = '{}'\
            \
            UNION ALL\
            \
            SELECT DISTINCT F.id_user_2, Conhece.nivel + 1\
            FROM Conhece, Friends F\
            WHERE Conhece.id2 = F.id_user_1\
                AND F.id_user_2 != '{}' \
                AND Conhece.nivel < 6 \
        )\
        SELECT U.name, MIN(nivel) FROM Conhece, Friends F, Users U \
        WHERE U.id = Conhece.id2 AND (nivel != 0 OR (F.id_user_1 = '{}' AND F.id_user_2 = Conhece.id2)) \
        GROUP BY U.name \
        ORDER BY MIN(nivel);".format(user_id, user_id, user_id)

    return fetch_from_query(query_cmd)
