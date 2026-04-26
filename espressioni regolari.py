
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

