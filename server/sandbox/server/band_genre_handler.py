from postgree import *


# return all genres from table band_has_genre
def get_all_genres():
    query_cmd = "SELECT b.genre_name, COUNT(*) AS Total \
        FROM band_has_genre b \
        GROUP BY b.genre_name \
        ORDER BY b.genre_name;"
    try:
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute(query_cmd)
            res = cursor.fetchall()
            genres = []
            for i in res:
                genres.append(i[0])
            return genres
        except Exception as e:
            print(e)
            return []
    except Exception as e:
        print(e)
        return []


# returns the genre_in_supergenre table
def get_supergenres_table():
    query_cmd = "SELECT * FROM genre_in_superset;"

    return fetch_from_query(query_cmd)


# returns how many bands each supergenre has
def get_count_bands_in_supergenres():
    query_cmd = "SELECT SP.superset_name, COUNT(*) AS Total \
        FROM genre_in_superset SP LEFT JOIN band_has_genre B \
        ON B.genre_name = SP.genre_name \
        GROUP BY SP.superset_name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


# returns how many genres each supergenre has
def get_count_genres_in_supergenres():
    query_cmd = "SELECT SP.superset_name, COUNT(*) AS Total \
        FROM genre_in_superset SP \
        GROUP BY SP.superset_name \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


# returns bands in both genres
def genres_intersection(genre_1, genre_2):

    query_cmd = "SELECT DISTINCT B.artistic_name \
        FROM bands B, band_has_genre BG1, band_has_genre BG2 \
        WHERE BG1.genre_name = '{}' AND BG2.genre_name = '{}' \
        AND BG2.id_band = BG1.id_band AND B.id = BG1.id_band \
        ORDER BY B.artistic_name;".format(
        genre_1, genre_2
    )

    return fetch_from_query(query_cmd)


# returns bands in both supergenres
def supergenres_intersection(supergenre_1, supergenre_2):

    query_cmd = "SELECT DISTINCT B.artistic_name \
        FROM bands B, \
        band_has_genre BG1, genre_in_superset S1, \
        band_has_genre BG2, genre_in_superset S2 \
        WHERE S2.superset_name = '{}' AND S1.superset_name = '{}' AND \
        BG1.genre_name = S1.genre_name AND BG2.genre_name = S2.genre_name \
        AND BG2.id_band = BG1.id_band AND B.id = BG1.id_band \
        ORDER BY B.artistic_name;".format(
        supergenre_1, supergenre_2
    )

    return fetch_from_query(query_cmd)


print(supergenres_intersection("rock", "k-pop"))
