from pytube import YouTube
import streamlit as st
import pandas as pd

link = input("Enter a link to download: ")
yt = YouTube(link)
downloader = yt.streams.get_highest_resolution()
print("Downloading...")
downloader.download(filename="video_download.mp4")
print("Finished downloading.")
