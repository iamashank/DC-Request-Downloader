"""
1. Youtube videos - 0
2. torrent links - 1
3. direct links - 2
4. anime - 3
5. songs (album) (torrent) - 4
6. softwares - (free, paid) - 5
"""
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from Youtube_downloader import Youtube_downloader
import os

class Dc_downloader:

	def __init__ (self, dlink, dtype, dname) :
		self.dlink = dlink
		self.dtype = dtype
		self.dname = dname
	

	def process_download(self):
		# Process dtype here
		if self.dtype == 0:
			# Process youtube downloads here
			youtube_downloader = Youtube_downloader(self.dlink)
			youtube_downloader.download()
			pass
		elif self.dtype == 1:
			# Process torrent downloads here
			pass
		elif self.dtype == 2:
			# Process direct downloads here
			try:
				os.system("wget " + self.dlink)
			except:
				print("no page found")
			pass
		elif self.dtype == 3:
			# Process anime downloads here
			pass
		elif self.dtype == 4:
			# Process songs downloads here
			pass
		elif self.dtype == 5:
			# Process software downloads here (free)
			pass
			self.free_software_download()
		elif self.dtype == 6:
			# Process software downloads here (paid)
			pass
		else:
			pass
			# Mark request for manual processing

	def direct_download(self):
		# Process download here
		pass

	def free_software_download(self):
		url = "http://filehippo.com/search?q="
		file_name = re.sub('\s+', '+', self.dname)
		url += file_name
		print (url)
		page = urlopen(url)


def main():
	# TODO implement command line parser and get input from user
	dlink = "http://www.tutorialspoint.com/python/python_tutorial.pdf"
	dtype = 2
	dname = "Gpythoo"
	download_link = dlink
	dowload_type = dtype
	download_name = dname
	dc_downloader = Dc_downloader(dlink, dtype, dname)
	dc_downloader.process_download()



if __name__ == '__main__':
	main()