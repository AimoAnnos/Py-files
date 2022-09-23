#13. Write a Python program that matches a word 
# containing 'z', not at the start or end of the word.

import re


def thirteen(string):
    pattern = re.compile(r'\w[^zZ]+\w[zZ]+\w[^zZ]+$')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)


thirteen("Song called Lazy is a good one by Deep Purple")
thirteen("Deep purple song called Lazy")
thirteen("Lazy is a good one by Deep Purple")