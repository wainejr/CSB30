# Relational Model

Obs.: **bold are primary keys**

User(**login**, name, hometown)

Block(**user**, **user_blocked**, reason) **user** -> User, **user_blocked** -> User

Friend(**user_1**, **user_2**) **user_1** -> User, **user_2** -> User

Movie(**id**, name, release_date, director, salary) director -> Person

Person(**name**, phone_number, address)

Act(**person**, **movie**, salary) **person** -> Person, **movie** -> Movie

Category(**name**, super_category) super_category -> Category

In(**movie**, **category**) **movie** -> Movie, **category** -> Category

LikesMovie(**user**, **movie**, rating) **user** -> User, **movie** -> Movie

MusicalArtist(**id**, artistic_name, country, musical_genre)

Musician(**name**, musical_genre, birthday)

Group(**musical_artist**) **musical_artist** -> MusicalArtist 

Singer(**musical_artist**, musician) **musical_artist** -> MusicalArtist, **musician** -> Musician

Duo(**musical_artist**) **musical_artist** -> MusicalArtist

GroupHas(**musician**, **group**) **musician** -> Musician, **group** -> Group

DuoHas(**musician**, **duo**) **musician** -> Musician, **duo** -> Duo

LikesArtist(**user**, **musical_artist**, rating) **user** -> User, **musical_artist** -> MusicalArtist