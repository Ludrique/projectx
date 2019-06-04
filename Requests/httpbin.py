import requests

#payload = {"page": 2, "count": 25}
#r = requests.get("https://httpbin.org/get", params=payload)
#print(r.url)

#payloads = {"username": "ludrick", "password": "testing"}
#p = requests.post("https://httpbin.org/post", data=payloads)
#p_dict = p.json()
#print(p_dict['form'])

#a = requests.get('https://httpbin.org/basic-auth/ludrick/testing', auth=('ludrick', 'testing'))
#print(a.text)

delay = requests.get('https://httpbin.org/delay/1', timeout=3)
print(delay)
