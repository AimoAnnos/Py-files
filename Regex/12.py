#12 Write a Python program that matches a word containing 'z'.

import re


def twelve(string):
    pattern = re.compile(r'[zZ]*\w*[zZ]+\w*')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)


twelve("Song called Lazy is a good one by Deep Purple")
twelve("Song called Gipsy is a good one by Deep Purple")
twelve("LaZy is a good one by Deep Purple")