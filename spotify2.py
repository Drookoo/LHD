import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

"""Lists the tracks in a playlist"""

# grabs the client ID and client secret stored environmental variables
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# authenticates and creates initializes the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_user():
    user = '1259237088'
    return user

results = sp.user_playlist_tracks(get_user(), playlist_id='2eNDAtuZErtgptlU1huKCv')

for result in results['items']:
    print(result['track']['name'])