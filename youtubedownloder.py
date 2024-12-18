from pytube import YouTube

link = input("Enter a link to download: ")
yt = YouTube(link)
downloader = yt.streams.get_highest_resolution()
print("Downloading...")
downloader.download(filename="video_download.mp4")
print("Finished downloading.")
