import streamlit as st
from dotenv import load_dotenv
from mcp_server import create_playlist

# Load environment variables
load_dotenv()

st.title("Playlist Generator")

activity = st.text_input("What is this playlist for? (e.g., workout, studying)")
vibe = st.text_area("Describe the vibe you're going for (e.g., energetic, calm, instrumental)")
languages = st.text_input("Enter preferred languages, separated by commas (e.g., English, Spanish, Hindi)", "English")

if st.button("Generate Playlist"):
    if activity and vibe:
        with st.spinner(f"Generating a playlist for {activity} with a {vibe} vibe..."):
            try:
                result = create_playlist(activity, vibe, languages)
                st.success(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please provide both an activity and a vibe description.")
