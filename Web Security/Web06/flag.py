import requests

url_cookie = 'http://web-06.challs.olicyber.it/token'

url_flag = 'http://web-06.challs.olicyber.it/flag'

session = requests.Session()

cookie = session.get(url_cookie)
print(cookie.cookies)

flag = session.get(url_flag, cookies=cookie.cookies)
print(flag.text)