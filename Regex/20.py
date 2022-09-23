#20 Write a Python program to search a literals string in a 
# string and also find the location
# within the original string where the pattern occurs.


import re

def twenty(string):    
    pattern = re.compile(r'fox')
    match = pattern.search(string)       
    print("\'fox\' found\nfrom:",match.start())
    print("to:",match.end())


twenty("The quick brown fox jumps over the lazy dog")