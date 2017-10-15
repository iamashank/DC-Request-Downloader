from pytube import YouTube
import pytube
youtube_link = "http://youtube.com/watch?v=9bZkp7q19f0"
print(youtube_link.split("?")[1][0])
if youtube_link.split("?")[1][0] == 'v':
	#download single video
	video = YouTube(youtube_link)
	video_quality = video.streams.first()
	print("downloading video")
	video_quality.download()
#elif youtube_link.split("?")[1][0] == 'l':
	#download youtube whole playlist