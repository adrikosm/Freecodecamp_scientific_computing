from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import json

url = 'https://www.crummy.com/software/BeautifulSoup/'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''

info = json.loads(data)
print(info[0]['name'])