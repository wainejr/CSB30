from postgree import *


# returns de average rating for all movies and the number of likes
def get_most_liked_movies():
    query_cmd = "SELECT M.title, AVG(LM.rating) AS Rating, COUNT(*) AS Total\
        FROM likes_movie LM, movies M \
        WHERE LM.id_movie = M.id\
        GROUP BY M.title \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


# returns de average rating for all director's movies and the number of movies
def get_most_popular_director():
    query_cmd = "SELECT M.director, AVG(LM.rating) AS Rating, COUNT(*) AS Total\
        FROM likes_movie LM, movies M \
        WHERE LM.id_movie = M.id\
        GROUP BY M.director \
        ORDER BY Total DESC;"

    return fetch_from_query(query_cmd)


# return all the movies by a director
def get_movies_by_director(director):
    query_cmd = "SELECT M.title \
        FROM movies M \
        WHERE M.director = '{}';".format(director)
    return fetch_from_query(query_cmd)


# return all directors
def get_all_directors():
    query_cmd = "SELECT M.director \
        FROM movies M \
        GROUP BY M.director \
        ORDER BY M.director;"
    return fetch_from_query(query_cmd)


# return all movies
def get_all_movies():
    query_cmd = "SELECT M.title \
        FROM movies M \
        GROUP BY M.title \
        ORDER BY M.title;"
    return fetch_from_query(query_cmd)


# return the average rating of the movies in a year and the total of movies
def get_movies_likes_by_date():
    query_cmd = "SELECT date_part('year', M.release_date) AS Year, AVG(LM.rating) AS Rating, COUNT(*) AS Total \
        FROM likes_movie LM, movies M \
        WHERE LM.id_movie = M.id \
        GROUP BY Year \
        ORDER BY Year;"
    return fetch_from_query(query_cmd)


# returns the number of likes in genres aNd its average
# and the number of movies in the genre
def get_movies_genres_likes():
    query_cmd = "SELECT MG.genre_name, AVG(LM.rating) AS Rating, COUNT(*) AS Total, \
        COUNT(M.title) AS TotalMovies \
        FROM likes_movie LM, movies M, movie_has_genre MG \
        WHERE LM.id_movie = M.id AND MG.id_movie = M.id \
        GROUP BY MG.genre_name \
        ORDER BY Total DESC;"
    return fetch_from_query(query_cmd)


# returns the number of movies in a genre
def get_count_movies_in_genres():
    query_cmd = "SELECT MG.genre_name, COUNT(*) AS Total \
        FROM movies M, movie_has_genre MG \
        WHERE MG.id_movie = M.id \
        GROUP BY MG.genre_name \
        ORDER BY Total DESC;"
    return fetch_from_query(query_cmd)


# returns movies in both genres
def get_movie_genres_intersection(genre_1, genre_2):
    query_cmd = "SELECT DISTINCT M.title \
        FROM movies M, movie_has_genre MG1, movie_has_genre MG2 \
        WHERE MG1.genre_name = '{}' AND MG2.genre_name = '{}' \
        AND MG2.id_movie = MG1.id_movie AND M.id = MG1.id_movie \
        ORDER BY M.title;".format(
        genre_1, genre_2
    )
    return fetch_from_query(query_cmd)


# returns the genres of a director
def get_director_genres(director):
    query_cmd = "SELECT MG.genre_name \
        FROM movies M, movie_has_genre MG \
        WHERE MG.id_movie = M.id AND M.director = '{}' \
        GROUP BY MG.genre_name \
        ORDER BY MG.genre_name DESC;".format(director)
    return fetch_from_query(query_cmd)
