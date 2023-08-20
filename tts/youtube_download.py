from pytube import YouTube

DOWNLOAD_FOLDER = "./whisper"
url = "https://www.youtube.com/watch?v=T--6HBX2K4g&ab_channel=KMUSIC"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
