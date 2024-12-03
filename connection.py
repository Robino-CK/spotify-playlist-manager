

# Import spotipy and spotify auth
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
# Set up the client id and client secret (you can find the client secret 
# from the spotify dev page)

with open('auth.json') as f:
  auth = json.load(f)
  
scope = "user-library-read"
auth_manager = SpotifyOAuth(client_id=auth["CLIENT_ID"], client_secret = auth["CLIENT_SECRET"], redirect_uri="http://localhost:8888/callback",scope=scope)
auth_url = auth_manager.get_authorize_url()
print(f"Open this URL in your browser to auth: {auth_url}")
sp = spotipy.Spotify(auth_manager=auth_manager)
print(sp.current_user())
results = sp.current_user_saved_tracks()
print(results)
#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " – ", track['name'])
    
CLIENT_ID = "[YOUR_SECRET]"