import requests
from bs4 import BeautifulSoup

# URL della risorsa da cui ottenere la flag
url = "http://web-01.challs.olicyber.it/"

# Eseguire una richiesta GET al server
response = requests.get(url)

# Verifica che la richiesta sia andata a buon fine
if response.status_code == 200:
    # Utilizza BeautifulSoup per analizzare il contenuto HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Stampa il contenuto della risposta
    print(soup.text)
else:
    print("Errore nella richiesta:", response.status_code)
