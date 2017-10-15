"""
1. Youtube videos - 0
2. torrent links - 1
3. direct links - 2
4. anime - 3
5. songs (album) (torrent) - 4
6. softwares - (free, paid) - 5
"""
class Dc_downloader:

	def __init__ (self, dlink, dtype, dname) :
		self.download_link = dlink
		self.dowload_type = dtype
		self.download_name = dname
	

	def process_download(self):
		# Check if dlink exists
		if not self.dlink:
			direct_download(self.dlink)
			return
		# Process dtype here
		if self.dtype == 0:
			# Process youtube downloads here
		elif self.dtype == 1:
			# Process torrent downloads here
		elif self.dtype == 2:
			# Process direct downloads here
		elif self.dtype == 3:
			# Process anime downloads here
		elif self.dtype == 4:
			# Process songs downloads here
		elif self.dtype == 5:
			# Process software downloads here
		else:
			# Mark request for manual processing

	def direct_download(self, dlink) :
		# Process download here



def main():
	# TODO implement command line parser and get input from user
	download_link = dlink
	dowload_type = dtype
	download_name = dname
	dc_downloader = Dc_downloader(dlink, dtype, dname)
	dc_downloader.process_download()



if __name__ == '__main__':
	main()