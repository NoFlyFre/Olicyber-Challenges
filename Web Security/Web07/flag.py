import requests

url = 'http://web-07.challs.olicyber.it/'

request = requests.head(url)

print(request.headers)