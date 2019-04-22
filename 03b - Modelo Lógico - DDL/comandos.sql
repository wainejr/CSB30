CREATE TABLE users
    (login TEXT NOT NULL,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL,
    PRIMARY KEY (login));

CREATE TABLE blocks
    (user_blocking TEXT NOT NULL,
    user_blocked TEXT NOT NULL,
    reason TEXT NOT NULL,
    FOREIGN KEY (user_blocking)
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (user_blocked) 
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (user_blocking, user_blocked));

CREATE TABLE friends
    (user_1 TEXT NOT NULL,
    user_2 TEXT NOT NULL,
    FOREIGN KEY (user_1)
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (user_2)
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (user_1, user_2));

CREATE TABLE people
    (name TEXT NOT NULL,
    phone_number INTEGER,
    address TEXT,
    PRIMARY KEY (name));

CREATE TABLE movies
    (id TEXT NOT NULL, -- changing id to TEXT to match URL format
    name TEXT NOT NULL,
    release_date DATE, -- changing release_date to DATE format
    director TEXT,
    salary DECIMAL,
    FOREIGN KEY (director)
        REFERENCES people(name)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    PRIMARY KEY (id));

CREATE TABLE act
    (person_1 TEXT NOT NULL,
    movie_id TEXT NOT NULL,
    salary DECIMAL NOT NULL,
    FOREIGN KEY (person_1) 
        REFERENCES people(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (movie_id)
        REFERENCES movies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (person_1, movie_id));

CREATE TABLE categories
    (name TEXT NOT NULL,
    super_category TEXT,
    FOREIGN KEY (super_category)
        REFERENCES categories(name)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    PRIMARY KEY (name));

CREATE TABLE incategory
    (movie_id TEXT NOT NULL,
    category TEXT,
    FOREIGN KEY (movie_id)
        REFERENCES movies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (category)
        REFERENCES categories(name)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    PRIMARY KEY (movie_id, category));

CREATE TABLE likesMovie
    (user_likes TEXT NOT NULL,
    movie_id TEXT NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_likes)
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (movie_id)
        REFERENCES movies(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (user_likes, movie_id));

CREATE TABLE musicalArtists
    (id TEXT NOT NULL, -- changing id to TEXT to match URL format
    artistic_name TEXT NOT NULL,
    country TEXT,
    musical_genre TEXT,
    PRIMARY KEY (id));

CREATE TABLE musicians
    (name TEXT NOT NULL,
    musical_genre TEXT,
    birthday DATE,
    PRIMARY KEY (name));

CREATE TABLE groups
    (musical_artist TEXT NOT NULL,
    FOREIGN KEY (musical_artist)
        REFERENCES musicalArtists(id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (musical_artist));

CREATE TABLE singer
    (musical_artist TEXT NOT NULL,
    musician TEXT NOT NULL,
    FOREIGN KEY (musical_artist)
        REFERENCES musicalArtists(id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (musician)
        REFERENCES musicians(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (musical_artist));

CREATE TABLE duo
    (musical_artist TEXT NOT NULL,
    FOREIGN KEY (musical_artist)
        REFERENCES musicalArtists(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (musical_artist));

CREATE TABLE groupHas
    (musician TEXT NOT NULL,
    group_name_id TEXT NOT NULL,
    FOREIGN KEY (musician)
        REFERENCES musicians(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (group_name_id)
        REFERENCES groups(musical_artist) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (musician, group_name_id));

CREATE TABLE duoHas
    (musician TEXT NOT NULL,
    duo_id TEXT NOT NULL,
    FOREIGN KEY (musician)
        REFERENCES musicians(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (duo_id)
        REFERENCES duo(musical_artist)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (musician, duo_id));

CREATE TABLE likesArtist
    (user_who_likes TEXT NOT NULL,
    musical_artist TEXT NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_who_likes)
        REFERENCES users(login)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (musical_artist)
        REFERENCES musicalArtists(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (user_who_likes, musical_artist));

INSERT INTO musicians VALUES ('Julian Casablancas', 'Rock', '1978-08-23');
INSERT INTO musicians VALUES ('Nick Valensi', 'Rock', '1981-01-16');
INSERT INTO musicians VALUES ('Nickolai Fraiture', 'Rock', '1978-11-13');

INSERT INTO musicians VALUES ('Kanye West', 'Rap', '1977-06-08');
INSERT INTO musicians VALUES ('Kid Cudi', 'Rap', '1984-01-30');

INSERT INTO musicians VALUES ('Ethan Kath', 'Synthpop', '1982-12-25');
INSERT INTO musicians VALUES ('Alice Glass', 'Synthpop', '1988-08-23');

INSERT INTO musicians VALUES ('Guy-Manuel de Homem-Christo', 'Eletronica', '1974-02-08');
INSERT INTO musicians VALUES ('Thomas Bangalter', 'Eletronica', '1975-01-03');

INSERT INTO musicians VALUES ('Marcelo de Souza Camelo', 'MPB', '1978-02-04');
INSERT INTO musicians VALUES ('Rodrigo Lins Martins', 'MPB', '1979-01-23');
INSERT INTO musicians VALUES ('Rodrigo Amarante de Castro Neves', 'MPB', '1976-09-06');
INSERT INTO musicians VALUES ('Bruno Medina', 'MPB', '1978-08-10');

INSERT INTO musicians VALUES ('Mallu Magalhaes', 'MPB', '1992-08-29');
INSERT INTO musicians VALUES ('Fred Pinto Ferreira', 'MPB', '1983-05-12');

INSERT INTO musicians VALUES ('Jahseh Dwayne Ricardo Onfroy', 'Trap', '1998-01-23');

INSERT INTO musicians VALUES ('Elizabeth Anne Harris', 'Experimental', '1980-03-15');

INSERT INTO musicians VALUES ('William Bevan', 'Eletronica', '1979-10-10');

INSERT INTO musicalArtists VALUES ('123456', 'The Strokes', 'USA', 'Rock');
INSERT INTO musicalArtists VALUES ('123457', 'Kids See Ghosts', 'USA', 'Rap');
INSERT INTO musicalArtists VALUES ('123458', 'Crystal Castles', 'Canada', 'Synthpop');
INSERT INTO musicalArtists VALUES ('123459', 'Daft Punk', 'Franca', 'Eletronica');
INSERT INTO musicalArtists VALUES ('123460', 'Los Hermanos', 'Brasil', 'MPB');
INSERT INTO musicalArtists VALUES ('123461', 'Banda do Mar', 'Brasil', 'MPB');
INSERT INTO musicalArtists VALUES ('123462', 'XXXTentacion', 'USA', 'Trap');
INSERT INTO musicalArtists VALUES ('123463', 'Grouper', 'USA', 'Experimental');
INSERT INTO musicalArtists VALUES ('123464', 'Burial', 'Inglaterra', 'Eletronica');

INSERT INTO singer VALUES ('123462', 'Jahseh Dwayne Ricardo Onfroy');
INSERT INTO singer VALUES ('123463', 'Elizabeth Anne Harris');
INSERT INTO singer VALUES ('123464', 'William Bevan');

INSERT INTO groups VALUES ('123456');
INSERT INTO groups VALUES ('123460');
INSERT INTO groups VALUES ('123461');

INSERT INTO duo VALUES ('123457');
INSERT INTO duo VALUES ('123458');
INSERT INTO duo VALUES ('123459');

INSERT INTO groupHas VALUES ('Julian Casablancas', '123456');
INSERT INTO groupHas VALUES ('Nick Valensi', '123456');
INSERT INTO groupHas VALUES ('Nickolai Fraiture', '123456');

INSERT INTO groupHas VALUES ('Marcelo de Souza Camelo', '123460');
INSERT INTO groupHas VALUES ('Rodrigo Lins Martins', '123460');
INSERT INTO groupHas VALUES ('Rodrigo Amarante de Castro Neves', '123460');
INSERT INTO groupHas VALUES ('Bruno Medina', '123460');

INSERT INTO groupHas VALUES ('Marcelo de Souza Camelo', '123461');
INSERT INTO groupHas VALUES ('Mallu Magalhaes', '123461');
INSERT INTO groupHas VALUES ('Fred Pinto Ferreira', '123461');

INSERT INTO duoHas VALUES ('Kanye West', '123457');
INSERT INTO duoHas VALUES ('Kid Cudi', '123457');

INSERT INTO duoHas VALUES ('Ethan Kath', '123458');
INSERT INTO duoHas VALUES ('Alice Glass', '123458');

INSERT INTO duoHas VALUES ('Guy-Manuel de Homem-Christo', '123459');
INSERT INTO duoHas VALUES ('Thomas Bangalter', '123459');

INSERT INTO users VALUES ('134', 'Amanda', 'Porto Alegre');
INSERT INTO users VALUES ('256', 'Mario', 'Rio de Janeiro');
INSERT INTO users VALUES ('379', 'José', 'Curitiba');
INSERT INTO users VALUES ('570', 'Bruna', 'Brasilia');

INSERT INTO likesArtist VALUES ('134', '123457', 5);
INSERT INTO likesArtist VALUES ('256', '123458', 4);
INSERT INTO likesArtist VALUES ('379', '123459', 3);

INSERT INTO likesArtist VALUES ('134', '123460', 5);
INSERT INTO likesArtist VALUES ('256', '123461', 5);
INSERT INTO likesArtist VALUES ('379', '123462', 4);

INSERT INTO people VALUES ('Francis Ford Coppola', 12930434, 'New York');
INSERT INTO people VALUES ('David Fincher', 39450434, 'Texas');
INSERT INTO people VALUES ('Christopher Nolan', 50630314, 'Washington');
INSERT INTO people VALUES ('Brad Pitt', 86549259, 'California');
INSERT INTO people VALUES ('Edward Norton', 10283849, 'New York');
INSERT INTO people VALUES ('Al Pacino', 29304819, 'Alabama');
    
INSERT INTO movies VALUES ('url/0', 'O Poderoso Chefão', '1980-10-22', 'Francis Ford Coppola', 100000);
INSERT INTO movies VALUES ('url/1', 'Batman: O Cavaleiro das Trevas', '2011-11-20', 'Christopher Nolan', 70000);
INSERT INTO movies VALUES ('url/2', 'Clube da Luta', '2001-02-11', 'David Fincher', 50000);

INSERT INTO categories VALUES ('Longa Metragem', NULL);
INSERT INTO categories VALUES ('Drama', 'Longa Metragem');
INSERT INTO categories VALUES ('Ação', 'Longa Metragem');

INSERT INTO incategory VALUES ('url/1', 'Longa Metragem');
INSERT INTO incategory VALUES ('url/1', 'Drama');
INSERT INTO incategory VALUES ('url/1', 'Ação');
INSERT INTO incategory VALUES ('url/0', 'Drama');
INSERT INTO incategory VALUES ('url/2', 'Drama');
INSERT INTO incategory VALUES ('url/2', 'Ação');

INSERT INTO likesMovie VALUES ('134', 'url/0', 10);
INSERT INTO likesMovie VALUES ('134', 'url/1', 9);
INSERT INTO likesMovie VALUES ('134', 'url/2', 8);
INSERT INTO likesMovie VALUES ('256', 'url/0', 8);
INSERT INTO likesMovie VALUES ('256', 'url/1', 7);
INSERT INTO likesMovie VALUES ('379', 'url/1', 10);

INSERT INTO act VALUES ('Edward Norton', 'url/2', 300000);
INSERT INTO act VALUES ('Brad Pitt', 'url/2', 350000);
INSERT INTO act VALUES ('Christopher Nolan', 'url/1', 400000);
INSERT INTO act VALUES ('Francis Ford Coppola', 'url/0', 200000);
INSERT INTO act VALUES ('David Fincher', 'url/2', 330000);
INSERT INTO act VALUES ('Al Pacino', 'url/0', 500000);

INSERT INTO blocks VALUES ('134', '256', 'I dont like him');
INSERT INTO blocks VALUES ('570', '134', 'He blocked me');
INSERT INTO blocks VALUES ('256', '379', 'I dont like him');
INSERT INTO blocks VALUES ('379', '134', 'He blocked me');
INSERT INTO blocks VALUES ('570', '256', 'I dont like him');
INSERT INTO blocks VALUES ('570', '379', 'He blocked me');

INSERT INTO friends VALUES ('134', '256');
INSERT INTO friends VALUES ('570', '134');
INSERT INTO friends VALUES ('256', '379');
INSERT INTO friends VALUES ('379', '134');
INSERT INTO friends VALUES ('570', '256');
INSERT INTO friends VALUES ('570', '379');
