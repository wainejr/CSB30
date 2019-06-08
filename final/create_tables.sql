CREATE TABLE users
    (id TEXT NOT NULL,
    name TEXT NOT NULL,
    hometown TEXT,
    PRIMARY KEY (id));

CREATE TABLE friends
    (id_user_1 TEXT NOT NULL,
    id_user_2 TEXT NOT NULL,
    FOREIGN KEY (id_user_1)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_user_2)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (id_user_1, id_user_2));

CREATE TABLE movies
    (id TEXT NOT NULL, -- changing id to TEXT to match URL format
    title TEXT NOT NULL,
    release_date DATE, -- changing release_date to DATE format
    director TEXT,
    rating INTEGER,
    PRIMARY KEY (id));

CREATE TABLE movie_has_genre
    (id_movie TEXT NOT NULL,
    genre_name TEXT NOT NULL,
    FOREIGN KEY (id_movie) 
        REFERENCES movies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (id_movie, genre_name));

CREATE TABLE likes_movie
    (user_likes TEXT NOT NULL,
    id_movie TEXT NOT NULL,
    rating INTEGER,
    FOREIGN KEY (user_likes)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_movie)
        REFERENCES movies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (user_likes, id_movie));

CREATE TABLE bands
    (id TEXT NOT NULL, -- changing id to TEXT to match URL format
    artistic_name TEXT NOT NULL,
    hometown TEXT,
    popularity INTEGER,
    followers INTEGER,
    url_img TEXT,
    PRIMARY KEY (id));

CREATE TABLE band_has_genre
    (id_band TEXT NOT NULL,
    genre_name TEXT NOT NULL,
    FOREIGN KEY (id_band) 
        REFERENCES bands(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (id_band, genre_name));

CREATE TABLE likes_band
    (id_user TEXT NOT NULL,
    id_band TEXT NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (id_user)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_band)
        REFERENCES bands(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (id_user, id_band));