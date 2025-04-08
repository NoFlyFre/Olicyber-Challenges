import requests

url_post = 'http://web-11.challs.olicyber.it/login'

url_flag = "http://web-11.challs.olicyber.it/flag_piece"

session = requests.Session()

credentials = {
    'username': 'admin',
    'password': 'admin'
}

flag = ""

for piece in range(0, 4):
    login = session.post(url_post, json=credentials)
    csrf = login.json()['csrf']
    params = {
        'csrf': csrf,
        'index': piece,
    }
    flag += session.get(url_flag, params=params).text.split()[2].replace("\"", "").replace(",", "")
    
print(flag)
    
    
    

