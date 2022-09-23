# 16. Write a Python program to remove leading zeros 
# from an IP address.

import re

def sixteen(string):
    res = re.sub(r'0','',string)    
    print(res)

sixteen("192.168.01.01")