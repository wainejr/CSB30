import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "e192baec5a7b8f6135a0945e8ecedc5c"  # this is a sample key
API_SECRET = "c25d6d4d8a8e882055e11ce6e4371080"

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)

# Now you can use that object everywhere
artist = network.get_artist("Swirlies")

print(artist.info)