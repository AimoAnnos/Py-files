#11.Write a Python program that matches a word 
# at the end of string, with optional punctuation
import re

def eleven(string):
    pattern = re.compile(r'\w+')
    matches = pattern.findall(string)
    res = matches[-1]
    print(res)

eleven("testing eleven")
eleven("testing eleven.")
eleven("testing eleven.word.")