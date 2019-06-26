from postgree import *


# return all genres from table band_has_genre
def get_all_genres():
    query_cmd = "SELECT b.genre_name, COUNT(*) AS Total \
        FROM band_has_genre b \
        GROUP BY b.genre_name \
        ORDER BY b.genre_name;"
    return fetch_from_query(query_cmd)


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
def get_genres_intersection(genre_1, genre_2):

    query_cmd = "SELECT DISTINCT B.artistic_name \
        FROM bands B, band_has_genre BG1, band_has_genre BG2 \
        WHERE BG1.genre_name = '{}' AND BG2.genre_name = '{}' \
        AND BG2.id_band = BG1.id_band AND B.id = BG1.id_band \
        ORDER BY B.artistic_name;".format(
        genre_1, genre_2
    )

    return fetch_from_query(query_cmd)


# returns bands in both supergenres
def get_supergenres_intersection(supergenre_1, supergenre_2):
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


# returns the number of likes in genres and its average
def get_genres_likes():
    query_cmd = "SELECT BG.genre_name, AVG(LB.rating) as Rating, \
            COUNT(*) as Total\
        FROM bands B, likes_band LB, band_has_genre BG \
        WHERE BG.id_band = LB.id_band AND B.id = LB.id_band\
        GROUP BY BG.genre_name \
        ORDER BY Total DESC;"
    return fetch_from_query(query_cmd)


# returns the number of followers of genres and the average popularity
def get_genres_sp_followers():
    query_cmd = "SELECT BG.genre_name, AVG(B.popularity) as Popularidade, \
            SUM(B.followers) as Followers \
        FROM bands B, likes_band LB, band_has_genre BG \
        WHERE BG.id_band = LB.id_band AND B.id = LB.id_band \
        GROUP BY BG.genre_name \
        ORDER BY Followers DESC;"
    return fetch_from_query(query_cmd)


# returns the number of likes in supergenres and its average
def get_supergenres_likes():
    query_cmd = "SELECT GS.superset_name, AVG(LB.rating) as Rating, \
            COUNT(*) as Total\
        FROM bands B, likes_band LB, band_has_genre BG, genre_in_superset GS \
        WHERE BG.id_band = LB.id_band AND B.id = LB.id_band AND \
            BG.genre_name = GS.genre_name\
        GROUP BY GS.superset_name \
        ORDER BY Total DESC;"
    return fetch_from_query(query_cmd)


# returns the number of followers of supergenres and the average popularity
def get_supergenres_sp_followers():
    query_cmd = "SELECT GS.superset_name, AVG(B.popularity) as Popularidade, \
            SUM(B.followers) as Followers \
        FROM bands B, likes_band LB, band_has_genre BG, genre_in_superset GS \
        WHERE BG.id_band = LB.id_band AND B.id = LB.id_band AND \
            BG.genre_name = GS.genre_name\
        GROUP BY GS.superset_name \
        ORDER BY Followers DESC;"
    return fetch_from_query(query_cmd)
