import json
import spotipy
import webbrowser
  
username = '31avmzearblyu3ry5vegfnur5bdq'
clientID = 'c86795318ddc42088b14052af07b6f57'
clientSecret = 'b671f9b385d04771999cacc4e2076fc9'
redirect_uri = 'http://localhost:8888/callback'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed
#print(json.dumps(user_name, sort_keys=True, indent=4))

results = spotifyObject.current_user_playlists(limit=50)
#print(json.dumps(results,sort_keys=True,indent=4))
for i, namu in enumerate(results['items']):
    print("%d %s" % (i,  namu['name']))
