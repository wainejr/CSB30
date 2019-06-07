import spotipy as sp
import spotipy.util as util

SPOTIPY_CLIENT_ID = "a2ceda076b844de8b08d037d86610795"
SPOTIPY_CLIENT_SECRET = "3ae6e178ecac4a2d848b7606c09e67d4"
SPOTIPY_REDIRECT_URI = "http://localhost/"


def getBandGenre(band_name):
    token = util.prompt_for_user_token(
        "Waine",
        "user-library-read",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
    )

    spotify = sp.Spotify(auth=token)
    search = spotify.search(q="artist:" + band_name, type="artist")
    id = search["artists"]["items"][0]["id"]
    artist = spotify.artist(artist_id=id)

    print(artist["genres"])
    return artist["genres"]
