import requests

url = 'http://web-08.challs.olicyber.it/login'

values = {
    'username': 'admin',
    'password': 'admin'
}

pr = requests.post(url, data=values)

print(pr.text)