#2. #Write a Python program that matches a string that has an
#  'a' followed by zero or more 'b' s.
import re


def two(string):
    res = re.match(r'^a(b*)$', string)
    return bool(res)

print(two("a"))    #True
print(two("ab"))   #True
print(two("abb"))  #True
print(two("abc"))  #False
print(two("ac"))   #False