import streamlit as st
from pytube import YouTube

# Set the title of the app
st.title("YouTube Video Downloader")

# Create a text input for the user to enter the YouTube link
link = st.text_input("Enter a link to download:")

if st.button("Download"):
    if link:
        try:
            # Create a YouTube object
            yt = YouTube(link)
            # Get the highest resolution stream
            downloader = yt.streams.get_highest_resolution()
            # Download the video
            st.write("Downloading...")
            downloader.download(filename="video_download.mp4")
            st.success("Finished downloading!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube link.")
