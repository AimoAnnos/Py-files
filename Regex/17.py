#17  Write a Python program to check for a 
# number at the end of a string (if there is one)

import re

def seventeen(string):
    pattern = re.compile(r'\w*[0-9]$') 
    matches = pattern.search(string)
    res = True if matches != None else False 
    print(res)


seventeen("testing")
seventeen("testing-1")
seventeen("testing-1-two-three")
seventeen("testing-1-two-three4")
seventeen("testing-1-two-three 400")
