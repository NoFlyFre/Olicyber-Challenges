import requests
from bs4 import BeautifulSoup

url='http://web-04.challs.olicyber.it/users'

headers = {
    'Accept': 'application/xml'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the XML content
    soup = BeautifulSoup(response.content, 'xml')
    
    print("Flag:", soup)
else:
    print("Failed to retrieve the flag. Status code:", response.status_code)
    print("Response content:", response.content)
