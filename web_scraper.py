# import the libraries
import pymongo
import requests
import json
from bs4 import BeautifulSoup


host = 'localhost'
database = 'firmware'
collection = 'product'


def main():
	
	url = 'https://www.rockchipfirmware.com/content/virgo-ace-tablet'
	
	# fetch raw html content
	page = requests.get(url)

	# parse the html content
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# firmware files to be downloaded are zip files
	filetype = '.zip'

	domain = 'https://www.rockchipfirmware.com/'
	


	'''

	for link in soup.findAll('a'):
		download = link.get('href')

		# isolate firmware file(s) to be downloaded
		if filetype in download:

			# some files have domain name
			link_clean = link.text.replace('http://www.rockchipfirmware.com/sites/default/files/', '')
			
			# download the file(s)
			with open(link_clean, 'wb') as file:
				response = requests.get(domain + download)
				file.write(response.content) 
	'''




	'''

	# Device name and Submitted by are hidden
	key_list = ['Device name', 'Submitted by']
	val_list = []
	
	# Add categories to list of keys
	for value in soup.findAll("div", {"class":"field-label"}):
		key_list.append(value.get_text()[:-2])
	
	# Add metadata (answers to categories) to list of values
	for value in soup.findAll("div", {"class":"field-item even"}):
		val_list.append(value.get_text())

	# create dictionary  with keys as categories and values as metadata
	final = {k : v for k,v in zip(key_list, val_list)}
	
	'''					

		
			



if __name__ == "__main__":
	main()
