"""

attenzione, potrebbe saturare la ram poiche salva tutto
il contenuto scaricato
in una variabile in una sola volta

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
"""

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
with open("cover3.jpg", "wb") as fhand:
    size = 0
    while True:
        info = img.read(10000)
        if len(info) < 1:
            break
        size = size + len(info)
        fhand.write(info)

print(size, "characters copied.")
