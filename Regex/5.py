#5. Write a Python program that matches a string that has an 'a' 
# followed by three 'b'.

import re



def five(string):
    res = re.match(r'^ab{3}?',string)
    return bool(res)


print(five("abbbb"))