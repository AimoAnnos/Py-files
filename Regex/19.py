#19. Write a Python program to search some literals 
# strings in a string.

import re

def nineteen(string):
    pattern = re.compile(r'fox|dog|horse')
    matches = pattern.findall(string)   
    for match in matches: 
        print(match)

nineteen("The quick brown fox jumps over the lazy dog")