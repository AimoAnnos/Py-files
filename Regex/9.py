#9.Write a Python program that matches a string that 
# has an 'a' followed by anything, ending in 'b'.

import re


def nine(string):
    pattern = re.compile(r'^a.*b$')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)
    

nine("aABCb")
nine("aBCDEbF")
nine("ab")