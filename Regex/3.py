#3. Write a Python program that matches a string that 
# has an 'a' followed by one or more b's
import re


def three(string):
    res = re.match(r'^[a][b]+$', string)
    #res = re.match(r'^a(b+)$', string) #alternative
    return bool(res)

print(three("aabbb"))     #False
print(three("abc"))       #False
print(three("abbbc"))     #False
print(three("bab"))       #False
print(three("abb"))       #True
print(three("ab"))        #True
print(three("abbbbbb"))    #True