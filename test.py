import requests

url = 'http://127.0.0.1:8000/addmsg'
myobj = {"time": "26/06/2022 21:42", "content": "sup bitch", "sender": "okb", "users": ["okb", "ad"]}
#url = 'http://127.0.0.1:8000/getmsg'
#myobj = {"users":["okb","moh"]}
#url = 'http://127.0.0.1:8000/moh'
#myobj = {"users":["okb","moh"]}


x = requests.post(url,json=myobj)

print(x.text)
