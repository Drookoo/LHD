import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
"""Lists all the playlists of the user"""

# grabs the client ID and client secret stored environmental variables
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# authenticates and creates initializes the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_user():
    user = '1259237088'
    return user

playlists = sp.user_playlists(get_user())

for playlist in playlists['items']:
    print("")
    print(playlist['name'])
    print('  total tracks', playlist['tracks']['total'])
    print("")
    print(playlist)