# import the libraries
import pymongo
import requests
import json
from bs4 import BeautifulSoup


host = 'localhost'
database = 'firmware'
collection = 'product'


def main():
	
	url = 'https://www.rockchipfirmware.com/node/267'
	
	# fetch raw html content
	page = requests.get(url)

	# parse the html content
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# firmware files to be downloaded are zip files
	filetype = '.zip'
	domain = 'https://www.rockchipfirmware.com/'
	
	for link in soup.findAll('a'):
		download = link.get('href')
		if filetype in download:

			# some files have domain name
			link_clean = link.text.replace('http://www.rockchipfirmware.com/sites/default/files/', '')
			
			with open(link_clean, 'wb') as file:
				response = requests.get(domain + download)
				file.write(response.content) 
	
	dict = {}
	
	

	#for value in soup.findAll("div", {"class":"field-item even"}):
            #print(value.get_text())



if __name__ == "__main__":
	main()
