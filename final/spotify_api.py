import spotipy as sp
import spotipy.util as util

SPOTIPY_CLIENT_ID = "a2ceda076b844de8b08d037d86610795"
SPOTIPY_CLIENT_SECRET = "3ae6e178ecac4a2d848b7606c09e67d4"
SPOTIPY_REDIRECT_URI = "http://localhost/"

def updateBandsInfo(table_band, table_band_has_genre, verbose=False):
    token = util.prompt_for_user_token(
        "Waine",
        "user-library-read",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
    )

    spotify = sp.Spotify(auth=token)
    for i in range(0, len(table_band)):
        band = table_band[i]
        if(len(band["values"]) > 3):
            continue
        # in band table: [id, name, hometown]
        # table_band=[id, name, hometown, popularity, followers, url_img]
        try:
            search = spotify.search(q=band["values"][1], type="artist")
            id = search["artists"]["items"][0]["id"]
            artist = spotify.artist(artist_id=id)
            # append populariy
            try:
                band["values"].append(artist['popularity'])
            except Exception as e:
                print(e)
                print("Error inserting popularity", band["values"][0])
                band["values"].append(None)
            # append folowers
            try:
                band["values"].append(artist['followers']['total'])
            except Exception as e:
                print(e)
                print("Error inserting followers", band["values"][0])
                band["values"].append(None)
            # append img url
            try:
                band["values"].append(artist['images'][0]['url'])
            except Exception as e:
                print(e)
                print("Error inserting image for id", band["values"][0])
                band["values"].append(None)
            try:
                for genre in artist['genres']:
                    table_band_has_genre.append(
                        {"values": [band["values"][0], genre]}
                    )
            except Exception as e:
                print(e)
                print("Error inserting genres for id")
            if(verbose):
                print(band["values"])
        except Exception as e:
            print(e)
            print("Error searching artist with id", band["values"][0])
        
        while(len(band["values"]) < 6): # needs 6 arguments
            band["values"].append(None)
        table_band[i] = band
