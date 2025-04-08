import requests
from bs4 import BeautifulSoup

url = "http://web-15.challs.olicyber.it/"

# Effettua la richiesta GET all'URL
req = requests.get(url)

# Crea un oggetto BeautifulSoup per l'analisi HTML
page = BeautifulSoup(req.text, 'html.parser')

links = page.find_all('link')
scripts = page.find_all('script')

for link in links:
    page = requests.get(f"{url}{link.attrs['href']}").text
    if "flag" in page:
        print(page)
        break
    
for script in scripts:
    page = requests.get(f"{url}{script.attrs['src']}").text
    if "flag" in page:
        print(page)
        break

