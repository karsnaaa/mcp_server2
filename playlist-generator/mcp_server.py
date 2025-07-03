import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_spotify_client():
    """Initializes and returns a Spotify client."""
    # Remove the cache file to force a new login every time
    try:
        os.remove(".cache")
    except FileNotFoundError:
        pass
        
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="playlist-modify-public",
        show_dialog=True
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def create_playlist(activity, vibe, languages="English"):
    """
    Creates a Spotify playlist based on activity, vibe, and a list of languages.
    """
    sp = get_spotify_client()
    user_id = sp.current_user()['id']
    
    # Create a new playlist
    playlist_name = f"{activity} ({vibe}) Playlist"
    playlist_description = f"A playlist for {activity} with a {vibe} vibe, featuring songs in {languages}."
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    
    track_uris = []
    language_list = [lang.strip() for lang in languages.split(',')]
    
    # Calculate number of tracks per language
    tracks_per_language = 20 // len(language_list)
    
    # Search for tracks for each language
    for lang in language_list:
        query = f"{vibe} {activity} {lang} songs"
        results = sp.search(q=query, type='track', limit=tracks_per_language)
        track_uris.extend([track['uri'] for track in results['tracks']['items']])

    # Add tracks to the playlist
    if track_uris:
        sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
        return f"Playlist '{playlist_name}' created successfully with songs in {languages}!"
    else:
        return f"Could not find any tracks for the vibe '{vibe}' in the specified languages. Please try a different search."

if __name__ == '__main__':
    # This is a placeholder for where the MCP server would be started
    # and the 'create_playlist' tool would be registered.
    print("MCP Server running...")
    # In a real MCP implementation, you would have a loop here
    # listening for tool calls.