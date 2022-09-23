#14. Write a Python program to match a string that contains 
# only upper and lowercase letters, numbers, and underscores
import re


def fourteen(string):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)


fourteen("ABCdef0123_abc")
fourteen("ABCde¤f0123_abc")
fourteen("!c")
fourteen("a:b:c")
fourteen("a_ b")