#10. Write a Python program that matches 
# a word at the beginning of a string.

import re


def ten_v1(string):
    pattern = re.compile(r'\w+')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)
    

ten_v1("Testing nr.10")
ten_v1("10 is being tested") #w also includes 0-9 and _
ten_v1("A tenth excercise")

def ten_v2(string):
    pattern = re.compile(r'^[a-zA-Z]+\s*')
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)
    

ten_v2("Testing nr.10")
ten_v2("10 is being tested") # here only letters accepted, followed by 0 or more hitespace(s)
ten_v2("A tenth excercise")