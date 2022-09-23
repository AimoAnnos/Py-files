#7. Write a Python program to find sequences of 
# lowercase letters joined with a underscore.

import re

def seven(string):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    matches = pattern.search(string)
    # if matches != None:
    #     print(matches[0])
    # else:
    #     print("no match")

    #or with ternary operation:
    res = matches[0] if matches != None else "no match"    
    print(res)

seven('aaa_bbbb')
seven('aaa_bbbbC')
seven('aaaB_bbbbC')
