# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tags = BeautifulSoup
counter2=0
def myFunc(link):
    counter1=0
    url = link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        counter1 += 1
        if counter1==position:
          global counter2
          counter2 += 1
          print("Retrieving: ", tag.get('href',None))
          if counter2 == count:
              break;
          else:
           myFunc(tag.get('href',None))



enterURL = input('Enter - ')
position = int(input("Enter Position: "))
count = int(input("Enter Count: "))
tags = myFunc(enterURL)
