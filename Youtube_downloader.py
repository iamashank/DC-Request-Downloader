from pytube import YouTube
import pytube

class Youtube_downloader:

	def __init__ (self, dlink) :
		self.dlink = dlink

	def download(self):
		youtube_link = self.dlink
		if youtube_link.split("?")[1][0] == 'v':
			#download single video
			video = YouTube(youtube_link)
			video_quality = video.streams.first()
			print("downloading video")
			video_quality.download()
		#elif youtube_link.split("?")[1][0] == 'l':
			#download youtube whole playlist