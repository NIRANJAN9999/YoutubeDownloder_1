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
            # Display available streams
            streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            stream_options = [f"{s.resolution} - {s.mime_type}" for s in streams]
            selected_stream = st.selectbox("Select a stream to download:", stream_options)

            # Get the selected stream
            if selected_stream:
                stream_index = stream_options.index(selected_stream)
                downloader = streams[stream_index]
                
                # Download the video
                st.write("Downloading...")
                downloader.download(filename="video_download.mp4")
                st.success("Finished downloading!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube link.")
