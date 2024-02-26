import urllib.request as UR
import json

url= input("Enter location: ")
print("Retrieving ", url)
data = UR.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
jsonn = json.loads(data)

sum = 0
total= 0

for comment in jsonn["comments"]:
    sum += int(comment["count"])
    total += 1

print('Count:', total)
print('Sum:', sum)
