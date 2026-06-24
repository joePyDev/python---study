"""
utilizzare le espressioni
regolari per cercare ed estrarre ripetutamente sottostringhe che
corrispondono a
un particolare pattern.


"""

# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
