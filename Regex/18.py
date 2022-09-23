#18 Write a Python program to search the numbers (0-9) of 
# length between 1 to 3 in a given string.

import re

def eightteen_v1(string):    
    matches = re.finditer(r'\d{1,3}',string)
    for match in matches:
        print(match.group(0)) #works here without 0 too    

#or
def eightteen_v2(string):
    pattern = re.compile(r'\d{1,3}') 
    matches = pattern.finditer(string)    
    for match in matches:
        print(match.group())


#eightteen_v1("number 1, 12, 13, and 345, not 4444")
#eightteen_v2("number 1, 12, 13, and 345, not 4444")


#exact match
def eightteen_v3(string):
    matches = re.findall(r'[\d]+',string) #also [0-9] OK
    for match in matches:        
        if(len(match))<4:
            print(match)
        

eightteen_v3("number 1, 12, 13, and 345, not 4444 or 88888")