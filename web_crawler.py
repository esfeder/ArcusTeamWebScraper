# import the libraries
import pymongo
import requests
import json
from bs4 import BeautifulSoup

host = 'localhost'
database = 'firmware'
collection = 'product'



def main():
	
	links = set()
	
	url = "https://www.rockchipfirmware.com/"
	ending = "firmware-downloads"
	current = 1

	while current <= 7:
	
		url = "https://www.rockchipfirmware.com/" + str(ending)

		# fetch raw html content
		page = requests.get(url)

		# parse the html content
		soup = BeautifulSoup(page.content, 'html.parser')


	
		for link in soup.findAll('a')[6:-14]:
		
			links.add(link.get('href'))
		
		if (current != 7):
			ending = soup.find(title="Go to next page").get('href')
			
		
		
		current += 1
		
	
	
	
	for each in links:
		
		if str(each).replace("\\", "/") == "cdn-cgi/l/email-protection":
			continue
		
		
		url = "https://www.rockchipfirmware.com/firmware-downloads" + "/" + str(each).replace("\\", "/")
		
		dict = {}
		
		# fetch raw html content
		page = requests.get(url)

		# parse the html content
		soup = BeautifulSoup(page.content, 'html.parser')
		
		
		for value in soup.findAll("div", {"class":"field-item even"}):
			print("test")

		
		
		
		
		
		
		
		
		
		
				
		
		

if __name__ == "__main__":
	main()

	




