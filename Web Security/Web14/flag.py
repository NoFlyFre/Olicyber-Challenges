import requests
from bs4 import BeautifulSoup

url = "http://web-14.challs.olicyber.it/"

# Effettua la richiesta GET all'URL
req = requests.get(url)

# Crea un oggetto BeautifulSoup per l'analisi HTML
page = BeautifulSoup(req.text, 'html.parser')

print(page)
