import requests

url = 'http://web-09.challs.olicyber.it/login'

data = {'username': 'admin', 'password': 'admin'}

pr = requests.post(url, headers={"Content-Type": "application/json"}, json=data)
print(pr.text)