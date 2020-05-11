import pymongo
import requests
from bs4 import BeautifulSoup

#Establish connection with default host and port 
client = MongoClient()

#Create database
db = client.firmware_db

#Create a collection
collection = db.firmware_collection


website = "https://www.rockchipfirmware.com/firmware-downloads"


result = requests.get(website)

print(result.status_code)

content = result.text

soup = BeautifulSoup(content, 'lxml')

print("kobe")
print(content)