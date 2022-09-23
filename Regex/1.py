# 1. Write a Python program to check that a string contains only a certain
#  set of characters (in this case a-z, A-Z and 0-9)

import re


def one_v1(string):
    pattern = re.compile(r'[a-zA-Z0-9]+$')
    res = pattern.match(string)
    return bool(res)


def one_v2(string):
    res = re.match(r'[a-zA-Z0-9]+$', string)
    return bool(res)

 
print(one_v1("1F"))
print(one_v2("1F"))