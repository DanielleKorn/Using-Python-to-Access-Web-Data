import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_301558.xml'
url = urllib.request.urlopen(address).read()
tree = ET.fromstring(url)

total = 0
#counts creats a list type object
counts = tree.findall('.//count')
print('User count:', len(counts))

for num in counts:
    number = int(num.text)
    total = total + number

print('Count:', total)
