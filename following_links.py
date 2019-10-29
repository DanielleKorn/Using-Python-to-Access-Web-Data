#This program uses urllib to read the HTML from the given URL and employ BeautifulSoup to make data more accessible
#Then, it extracts the href= vaues from the anchor tags, scans for a tag that is in a particular position relative to the first name in the list
#And follows that link, repeating the process a number of times until reporting the last name found

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("Enter url:")
count=int(input('Enter count:'))
pos=int(input('Enter position:'))-1

urllist=list()

for i in range(count):
    html=urllib.request.urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print('Retrieveing:',url)
    taglist=list()
    for tag in tags:
        y=tag.get('href',None)
        taglist.append(y)

    url=taglist[pos]

    urllist.append(url)

print("Last Url:",urllist[-2])
