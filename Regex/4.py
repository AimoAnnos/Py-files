#4. Write a Python program that matches a string that 
# has an 'a' followed by zero or one 'b'.
import re


def four(string):
    res = re.match(r'^a(b)?$', string)   
    return bool(res)

print(four("a"))
print(four("ab"))
print(four("abb"))
