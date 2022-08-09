import socket
#crea el socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#hacer conexion con el servidor web
mysock.connect(('data.pr4e.org',80))
#encode() decodificar el caracter en UFT-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
#recv() se utiliza para recibir informacion
    data = mysock.recv(215)

    if (len(data) < 1):
        break
#decodifica los datos de python
    print(data.decode())
mysock.close()


import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts= dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1

print(counts)

#busca los enlaces en el python

url = 'http://www.dr-chuck.com/page1.html'
#abre la página web y comienza a leer
html = urllib.request.urlopen(url).read()
#seleccion todo el html
soup = BeautifulSoup(html,'html.parser')
#imprime tola la página
print(soup.prettify())
#este enlace te eseñara lo basico  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#muestrame lo hipervinculos
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

#muestra toda la pagina web
