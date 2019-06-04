import requests

r = requests.get("https://xkcd.com/353/")
#print(dir(r))

i = requests.get("https://xkcd.com/comics/python.png")
with open('comic.png', 'wb') as f:
    f.write(i.content)
