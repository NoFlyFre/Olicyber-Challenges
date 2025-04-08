import requests
from bs4 import BeautifulSoup 

url = "http://web-12.challs.olicyber.it/."

req  = requests.get(url)
page = BeautifulSoup(req.text, 'html.parser')
print(page)