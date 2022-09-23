#8. Write a Python program to find the sequences of 
# one upper case letter followed by lower case letters.
import re

def eight(string):
    pattern = re.compile(r'^[A-Z][a-z]+$')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)


eight("Abbb")
eight("AbbbCCC")
eight("ABcD")
eight("AAb")