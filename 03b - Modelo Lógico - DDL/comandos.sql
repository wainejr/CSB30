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
    (user_1 TEXT NOT NULL REFERENCES users(login),
    user_2 TEXT NOT NULL REFERENCES users(login),
    PRIMARY KEY (user_1, user_2));

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
    musician TEXT NOT NULL REFERENCES musicians(name),
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

INSERT INTO musicians VALUES ('Julian Casablancas', 'Rock', 23081978);
INSERT INTO musicians VALUES ('Nick Valensi', 'Rock', 16011981);
INSERT INTO musicians VALUES ('Nickolai Fraiture', 'Rock', 13111978);

INSERT INTO musicians VALUES ('Kanye West', 'Rap', 08061977);
INSERT INTO musicians VALUES ('Kid Cudi', 'Rap', 30011984);

INSERT INTO musicians VALUES ('Ethan Kath', 'Synthpop', 25121982);
INSERT INTO musicians VALUES ('Alice Glass', 'Synthpop', 23081988);

INSERT INTO musicians VALUES ('Guy-Manuel de Homem-Christo', 'Eletronica', 08021974);
INSERT INTO musicians VALUES ('Thomas Bangalter', 'Eletronica', 03011975);

INSERT INTO musicians VALUES ('Marcelo de Souza Camelo', 'MPB', 04021978);
INSERT INTO musicians VALUES ('Rodrigo Lins Martins', 'MPB', 23011979);
INSERT INTO musicians VALUES ('Rodrigo Amarante de Castro Neves', 'MPB', 06091976);
INSERT INTO musicians VALUES ('Bruno Medina', 'MPB', 10081978);

INSERT INTO musicians VALUES ('Mallu Magalhaes', 'MPB', 29081992);
INSERT INTO musicians VALUES ('Fred Pinto Ferreira', 'MPB', 12051983);

INSERT INTO musicians VALUES ('Jahseh Dwayne Ricardo Onfroy', 'Trap', 23011998);

INSERT INTO musicians VALUES ('Elizabeth Anne Harris', 'Experimental', 15031980);

INSERT INTO musicians VALUES ('William Bevan', 'Eletronica', 10101979);

INSERT INTO musicalArtists VALUES (123456, 'The Strokes', 'USA', 'Rock');
INSERT INTO musicalArtists VALUES (123457, 'Kids See Ghosts', 'USA', 'Rap');
INSERT INTO musicalArtists VALUES (123458, 'Crystal Castles', 'Canada', 'Synthpop');
INSERT INTO musicalArtists VALUES (123459, 'Daft Punk', 'Franca', 'Eletronica');
INSERT INTO musicalArtists VALUES (123460, 'Los Hermanos', 'Brasil', 'MPB');
INSERT INTO musicalArtists VALUES (123461, 'Banda do Mar', 'Brasil', 'MPB');
INSERT INTO musicalArtists VALUES (123462, 'XXXTentacion', 'USA', 'Trap');
INSERT INTO musicalArtists VALUES (123463, 'Grouper', 'USA', 'Experimental');
INSERT INTO musicalArtists VALUES (123464, 'Burial', 'Inglaterra', 'Eletronica');

INSERT INTO singer VALUES (123462, 'Jahseh Dwayne Ricardo Onfroy');
INSERT INTO singer VALUES (123463, 'Elizabeth Anne Harris');
INSERT INTO singer VALUES (123464, 'William Bevan');

INSERT INTO groups VALUES (123456);
INSERT INTO groups VALUES (123460);
INSERT INTO groups VALUES (123461);
INSERT INTO duo VALUES (123457);
INSERT INTO duo VALUES (123458);
INSERT INTO duo VALUES (123459);

INSERT INTO groupHas VALUES ('Julian Casablancas', 123456);
INSERT INTO groupHas VALUES ('Nick Valensi', 123456);
INSERT INTO groupHas VALUES ('Nickolai Fraiture', 123456);

INSERT INTO groupHas VALUES ('Marcelo de Souza Camelo', 123460);
INSERT INTO groupHas VALUES ('Rodrigo Lins Martins', 123460);
INSERT INTO groupHas VALUES ('Rodrigo Amarante de Castro Neves', 123460);
INSERT INTO groupHas VALUES ('Bruno Medina', 123460);

INSERT INTO groupHas VALUES ('Marcelo de Souza Camelo', 123461);
INSERT INTO groupHas VALUES ('Mallu Magalhaes', 123461);
INSERT INTO groupHas VALUES ('Fred Pinto Ferreira', 123461);

INSERT INTO duoHas VALUES ('Kanye West', 123457);
INSERT INTO duoHas VALUES ('Kid Cudi', 123457);

INSERT INTO duoHas VALUES ('Ethan Kath', 123458);
INSERT INTO duoHas VALUES ('Alice Glass', 123458);

INSERT INTO duoHas VALUES ('Guy-Manuel de Homem-Christo', 123459);
INSERT INTO duoHas VALUES ('Thomas Bangalter', 123459);

INSERT INTO likesArtist VALUES (134, 123457, 5);
INSERT INTO likesArtist VALUES (256, 123458, 4);
INSERT INTO likesArtist VALUES (379, 123459, 3);

INSERT INTO likesArtist VALUES (134, 123460, 5);
INSERT INTO likesArtist VALUES (256, 123461, 5);
INSERT INTO likesArtist VALUES (379, 123462, 4);

INSERT INTO users VALUES ("134", "Amanda", "Porto Alegre");
INSERT INTO users VALUES ("256", "Mario", "Rio de Janeiro");
INSERT INTO users VALUES ("379", "José", "Curitiba");
    
INSERT INTO movies VALUES (0, "O Poderoso Chefão", 85013246, "Francis Ford Coppola", 100000);
INSERT INTO movies VALUES (1, "Batman: O Cavaleiro das Trevas", 1216421246, "Christopher Nolan", 70000);
INSERT INTO movies VALUES (2, "Clube da Luta", 941237246, "David Fincher", 50000);

INSERT INTO people VALUES ("Francis Ford Coppola", 1293043456, "New York");
INSERT INTO people VALUES ("David Fincher", 3945043456, "Texas");
INSERT INTO people VALUES ("Christopher Nolan", 5063031469, "Washington");
INSERT INTO people VALUES ("Brad Pitt", 8654925925, "California");
INSERT INTO people VALUES ("Edward Norton", 1028384959, "New York");
INSERT INTO people VALUES ("Al Pacino", 2930481920, "Alabama");

INSERT INTO act VALUES ("Edward Norton", 2, 300000);
INSERT INTO act VALUES ("Brad Pitt", 2, 350000);
INSERT INTO act VALUES ("Christopher Nolan", 1, 400000);
INSERT INTO act VALUES ("Francis Ford Coppola", 0, 200000);
INSERT INTO act VALUES ("David Fincher", 2, 330000);
INSERT INTO act VALUES ("Al Pacino", 0, 500000);

INSERT INTO categories VALUES ("Longa Metragem", NULL);
INSERT INTO categories VALUES ("Drama", "Longa Metragem");
INSERT INTO categories VALUES ("Ação", "Longa Metragem");

INSERT INTO incategory VALUES (1, "Longa Metragem");
INSERT INTO incategory VALUES (1, "Drama");
INSERT INTO incategory VALUES (1, "Ação");
INSERT INTO incategory VALUES (0, "Drama");
INSERT INTO incategory VALUES (2, "Drama");
INSERT INTO incategory VALUES (2, "Ação");

INSERT INTO likesMovie VALUES ("134", 0, 10);
INSERT INTO likesMovie VALUES ("134", 1, 9);
INSERT INTO likesMovie VALUES ("134", 2, 8);
INSERT INTO likesMovie VALUES ("256", 0, 8);
INSERT INTO likesMovie VALUES ("256", 0, 7);
INSERT INTO likesMovie VALUES ("379", 1, 10);

INSERT INTO blocks VALUES ("134", "256", "I don't like him");
INSERT INTO blocks VALUES ("256", "134", "He blocked me");
INSERT INTO blocks VALUES ("134", "379", "I don't like him");
INSERT INTO blocks VALUES ("379", "134", "He blocked me");
INSERT INTO blocks VALUES ("379", "256", "I don't like him");
INSERT INTO blocks VALUES ("256", "379", "He blocked me");

INSERT INTO friends VALUES ("134", "256");
INSERT INTO friends VALUES ("256", "134");
INSERT INTO friends VALUES ("134", "379");
INSERT INTO friends VALUES ("379", "134");
INSERT INTO friends VALUES ("379", "256");
INSERT INTO friends VALUES ("256", "379");