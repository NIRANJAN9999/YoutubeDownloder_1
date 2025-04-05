import streamlit as st
import yt_dlp
from datetime import datetime

# Set the title of the app
st.title("YouTube Video Downloader")

# Create a text input for the user to enter the YouTube link
link = st.text_input("Enter a link to download:")

if st.button("Download"):
    if link:
        try:
            # Set up options for yt-dlp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"video_download_{timestamp}.mp4"  # Unique filename
            
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
                'merge_output_format': 'mp4',          # Merge into mp4 format
                'outtmpl': output_filename,             # Output filename
            }

            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                st.write("Downloading...")
                ydl.download([link])
                st.success(f"Finished downloading as {output_filename}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube link.")
