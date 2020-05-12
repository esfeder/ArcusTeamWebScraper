# import the libraries
import pymongo
import requests
import json
from bs4 import BeautifulSoup

host = 'localhost'
database = 'firmware'
collection = 'product'



def main():
	
	url = "https://www.rockchipfirmware.com/node/267"
	
	# fetch raw html content
	page = requests.get(url)

	# parse the html content
	soup = BeautifulSoup(page.content, 'html.parser')


	
	for link in soup.findAll('a')[6:-14]:
		
		links.add(link.get('href'))
		

	
	for value in soup.findAll("div", {"class":"field-item even"}):
            print("test")



if __name__ == "__main__":
	main()
