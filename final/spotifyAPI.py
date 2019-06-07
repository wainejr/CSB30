import spotipy as sp
import spotipy.util as util
import os

SPOTIPY_CLIENT_ID='a2ceda076b844de8b08d037d86610795'
SPOTIPY_CLIENT_SECRET='3ae6e178ecac4a2d848b7606c09e67d4'
SPOTIPY_REDIRECT_URI='http://localhost/'

token = util.prompt_for_user_token("Waine", "user-library-read",
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)

name = "Red Hot Chili Peppers"
spotify = sp.Spotify(auth=token)
search = spotify.search(q='artist:' + name, type='artist')
id = search["artists"]["items"][0]["id"]
artist = spotify.artist(artist_id=id)

# print(artist)

dict_artist = {}
dict_artist['genres'] = artist['genres']
dict_artist['followers'] = artist['followers']['total']
dict_artist['popularity'] = artist['popularity']
dict_artist['img_url'] = artist['images'][0]['url']

print(dict_artist)
