import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = 'http://py4e-data.dr-chuck.net/comments_1219239.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall("comments/comment")
pp = list()
for item in lst:
    pp.append(item.find("count").text)
for i in range(len(pp)):
    pp[i] = int(pp[i])
print(sum(pp))
