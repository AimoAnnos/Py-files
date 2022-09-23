#6. Write a Python program that matches a string that 
# has an 'a' followed by two to three 'b'.

import re



def six(string):
    res = re.match(r'^ab{2,3}?',string)
    return bool(res)


print(six("abbc"))