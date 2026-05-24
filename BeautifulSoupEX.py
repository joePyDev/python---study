"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re


url = "https://www.dr-chuck.com/"         # input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')





# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    

# https://www.dr-chuck.com/    
    

"""



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re


url = "https://www.dr-chuck.com/"         # input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


href= '".+"' # cerca l'url

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    tag = str(tag)    
    ricerca_regex = re.findall(href,tag)
    print(ricerca_regex)
    