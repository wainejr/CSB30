CREATE TABLE users
    (login TEXT NOT NULL,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL,
    PRIMARY KEY (login));

CREATE TABLE blocks
    (user_blocking TEXT NOT NULL REFERENCES users(login),
    user_blocked TEXT NOT NULL REFERENCES users(login),
    reason TEXT NOT NULL,
    PRIMARY KEY (user_blocking, user_blocked));

CREATE TABLE friends
    (user_blocking TEXT NOT NULL REFERENCES users(login),
    user_blocked TEXT NOT NULL REFERENCES users(login),
    reason TEXT NOT NULL,
    PRIMARY KEY (user_blocking, user_blocked));

CREATE TABLE people
    (name TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    adress TEXT NOT NULL,
    PRIMARY KEY (name));

CREATE TABLE movies
    (id INTEGER NOT NULL,
    name TEXT NOT NULL,
    release_date INTEGER NOT NULL,
    director TEXT NOT NULL REFERENCES people(name),
    salary DECIMAL NOT NULL,
    PRIMARY KEY (id));

CREATE TABLE act
    (person_1 TEXT NOT NULL REFERENCES people(name),
    movie_id INTEGER NOT NULL REFERENCES movies(id),
    salary DECIMAL NOT NULL,
    PRIMARY KEY (person_1, movie_id));

CREATE TABLE categories
    (name TEXT NOT NULL,
    super_category TEXT REFERENCES categories(name),
    PRIMARY KEY (name));

CREATE TABLE incategory
    (movie_id INTEGER NOT NULL REFERENCES movies(id),
    category TEXT NOT NULL REFERENCES categories(name),
    PRIMARY KEY (movie_id, category));

CREATE TABLE likesMovie
    (user_likes TEXT NOT NULL REFERENCES users(login),
    movie_id INTEGER NOT NULL REFERENCES movies(id),
    rating INTEGER NOT NULL,
    PRIMARY KEY (user_likes, movie_id));

CREATE TABLE musicalArtists
    (id INTEGER NOT NULL,
    artistic_name TEXT NOT NULL,
    country TEXT NOT NULL,
    musical_genre TEXT NOT NULL,
    PRIMARY KEY (id));

CREATE TABLE musicians
    (name TEXT NOT NULL,
    musical_genre TEXT NOT NULL,
    birthday INTEGER NOT NULL,
    PRIMARY KEY (name));

CREATE TABLE groups
    (musical_artist INTEGER NOT NULL REFERENCES musicalArtists(id),
    PRIMARY KEY (musical_artist));

CREATE TABLE singer
    (musical_artist INTEGER NOT NULL REFERENCES musicalArtists(id),
    PRIMARY KEY (musical_artist));

CREATE TABLE duo
    (musical_artist INTEGER NOT NULL REFERENCES musicalArtists(id),
    PRIMARY KEY (musical_artist));

CREATE TABLE groupHas
    (musician TEXT NOT NULL REFERENCES musicians(name),
    group_name_id INTEGER NOT NULL REFERENCES groups(musical_artist),
    PRIMARY KEY (musician, group_name_id));

CREATE TABLE duoHas
    (musician TEXT NOT NULL REFERENCES musicians(name),
    duo_id INTEGER NOT NULL REFERENCES duo(musical_artist),
    PRIMARY KEY (musician, duo_id));

CREATE TABLE likesArtist
    (user_likes TEXT NOT NULL REFERENCES users(login),
    musical_artist INTEGER NOT NULL REFERENCES musicalArtists(id),
    rating INTEGER NOT NULL,
    PRIMARY KEY (user_likes, musical_artist));