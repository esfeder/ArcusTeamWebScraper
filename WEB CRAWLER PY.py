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

		soup.prettify()
	

		table = soup.find('table')
		
		table_rows = table.find_all('tr')

		#for tr in table_rows:
			#a = tr.find_all('a')
			#row = [i.text.strip() for i in a]
			#print(row)
	
		for link in soup.findAll('a')[6:-14]:
			links.add(link.get('href'))
		
		if (current != 7):
			ending = soup.find(title="Go to next page").get('href')
			print(ending)
		
		
		current += 1
	
	
	links.remove('cdn-cgi\\l\\email-protection')
	
	for each in links:
		
		

if __name__ == "__main__":
	main()

	




