import requests
from bs4 import BeautifulSoup

url = "http://web-13.challs.olicyber.it/"

# Effettua la richiesta GET all'URL
req = requests.get(url)

# Crea un oggetto BeautifulSoup per l'analisi HTML
page = BeautifulSoup(req.text, 'html.parser')

# Usa find_all per cercare tutti i tag 'span'
spans = page.find_all('span')

flag = "flag{"

for span in spans:
    # Stampa il contenuto di ogni tag 'span'
    flag += span.text
    
flag += "}"
print(flag)

