# Devi esaminare tutti i tag <comment> e trovare la somma dei valori <count>.

"""
<commento>
  <nome>Mattia</nome>
  <count>97</count>
</comment>
"""

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")
tree = ET.fromstring(data)

counts = tree.findall(".//count")
nums = list()
somma = 0
for result in counts:
    nums.append(result.text)
    somma = somma + int(result.text)

print("Count:", len(nums))
print("Sum:", somma)
