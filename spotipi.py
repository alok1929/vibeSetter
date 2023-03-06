import json
import os
from dotenv import load_dotenv
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
  
username = '31avmzearblyu3ry5vegfnur5bdq'
clientID = 'c86795318ddc42088b14052af07b6f57'
clientSecret = 'b671f9b385d04771999cacc4e2076fc9'
redirect_uri = 'http://localhost:8888/callback'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
spotify=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(clientID,clientSecret))


playlist_id='3Tgx02eWZsRL9k5FCLQKCV'
results = spotify.playlist_items(playlist_id, fields="items.track.id,items.track.name,total")
#print(json.dumps(spotify.playlist_items,sort_keys=True,indent=4))
for i, item in enumerate(results['items']):
    track = item['track']
    track_info = spotify.track(track['id'])
    track_url = track_info['external_urls']['spotify']
    webbrowser.open(track_url)
    break


#the problem that arises is that songs cant be played using spotipy because it is just webpack that gives u data, so we must use flask to create a standalone application to play songs.

