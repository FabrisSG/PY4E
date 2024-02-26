'''El programa usará urllib para leer el HTML de los archivos de datos a
continuación y analizar los datos, extraer números y calcular la suma de los
 números en el archivo.'''


import urllib.request
import urllib.parse
import urllib.error
import bs4
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1219237.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    sum = sum+int(tag.contents[0])
print(sum)
