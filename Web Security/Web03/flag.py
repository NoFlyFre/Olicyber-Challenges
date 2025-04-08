import requests
import bs4

url = 'http://web-03.challs.olicyber.it/flag'

headers = {
    'X-Password': 'admin'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the HTML content
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    print("Flag:", soup)
else:
    print("Failed to retrieve the flag. Status code:", response.status_code)
    print("Response content:", response.content)
# This code sends a GET request to the specified URL with the required header
# and then parses the HTML response to extract the flag text.           