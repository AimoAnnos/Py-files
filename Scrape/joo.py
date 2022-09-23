from operator import le
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)

print(len(page.text))
print(len(page.content))
