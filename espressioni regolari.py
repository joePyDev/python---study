
# espressioni regolari:


# funzione serch()

import re

r"""
hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:",line):
        print(line)



# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^F..m:",line):
        print(line)
        
"""

# * 0 o piu volte, greedy 
# + 1 o piu volte, greedy
# *? : Zero o più caratteri, ma il minor numero possibile. lazy
# +? : Uno o più caratteri, ma il minor numero possibile. lazy

hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:.+@",line):
        print(line)





r"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

"""

# funzione serch()
import re



r"""

hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:",line):
        print(line)



# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^F..m:",line):
        print(line)
        


# * 0 o piu volte, greedy 
# + 1 o piu volte, greedy
# *? : Zero o più caratteri, ma il minor numero possibile. lazy
# +? : Uno o più caratteri, ma il minor numero possibile. lazy

hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search(r"^From:.+@",line):
        print(line)






# findall(  [le parentesi ritornano il contenuto se in findall]    ) 

s = "A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM"
# Add the 'r' prefix here
lst = re.findall(r"\S+@\S+", s) 
print(lst)


hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]",line)
    if len(x) > 0:
        print(x)

"""




hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("^X-\S*: [0-9.]+",line)
    if len(x) > 0:
        print(x)




hand = open(r"mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("^X\S*: ([0-9.]+)",line)
    if len(x) > 0:
        print(x)



# il backlash permette di cercare il carattere stesso:
    
import re
X = "abbiamo ricevuto $10000 di biscotti"
y = re.findall("\$[0-9]+", X)


print(help(re))



x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)



B = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
C = re.search('\S+?@\S+',B)


print(C)
