#15  Write a Python program where a 
# string will start with a specific number (f.ex. 10)

import re

def fifteen(string):
    pattern = re.compile(r'^10\s+.*$') #here 10 has to match exactly
    #pattern = re.compile(r'^10') #here also f.ex.100 is okay
    matches = pattern.search(string)
    res = matches[0] if matches != None else "no match"    
    print(res)


fifteen("10 out of 10")
fifteen("1 out of 10")
fifteen("100 out of 100")
fifteen("that's 10 out of 10")
