import requests as req
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

response = req.get(input("url that you wanna test for rickrolls: "), headers = HEADERS)

#print(response)
#print(dir(response))

soup = BeautifulSoup(response.content, features="lxml")

#print(soup.select("body"))

if "dQw4w9WgXcQ" in response.content.decode("utf-8"):
    print("Watch out!! This website contains rickroll link!")
else:
    print("didn't find any rickroll links")
