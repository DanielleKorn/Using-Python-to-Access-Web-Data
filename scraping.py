#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:
#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#You need to adjust this code to look for span tags and pull out the text content of the span tag,
#convert them to integers and add them up to complete the assignment.

import urllib.request , urllib.parse , urllib.error
import ssl
from bs4 import BeautifulSoup
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_301556.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

total = 0
span = soup('span')
for line in span:
    line = line.decode()
    num = re.findall('[0-9]+', line)
    numstr = num[0]
    int = float(numstr)
    total = total + int

print(total)
