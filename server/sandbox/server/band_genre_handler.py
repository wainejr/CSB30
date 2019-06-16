from postgree import *


SUPERGENRES = {  # name_super: [words]
    "rock": ["rock"],
    "rap": ["rap"],
    "pop": ["pop"],
    "hip hop": ["hip hop", "hip-hop", "hiphop"],
    "metal": ["metal"],
    "folk": ["folk"],
    "punk": ["punk"],
    "indie": ["indie"],
    "edm": ["edm"],
    "reggae": ["reggae"],
    "funk": ["funk"],
    "soul": ["soul"],
    "r&b": ["r&b"],
    "blues": ["blues"],
    "symphonic": ["symphonic"],
    "classical": ["classical"],
    "contemporary": ["contemporary"],
    "electro": ["electro"],
    "grunge": ["grunge"],
    "jazz": ["jazz"],
    "house": ["house"],
    "dance": ["dance"],
    "country": ["country"],
    "trap": ["trap"],
    "latin": ["latin"],
    "trash": ["trash"],
    "emo": ["emo"],
    "k-pop": ["k-pop"],
    "j-pop": ["j-pop"],
    "mpb": ["mpb"],
    "sertanejo": ["sertanejo"],
    "samba": ["samba"],
    "pagode": ["pagode"],
    "forro": ["forro"],
    "bossa nova": ["bossa nova"],
    "brasileiro": ["brazilian", "brasileiro", "brasileira"],
}

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
