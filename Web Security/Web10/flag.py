import requests

url = 'http://web-10.challs.olicyber.it/'

request = requests.put(url)


print(request.headers)
print(request)

