import requests
from bs4 import BeautifulSoup
import sys

res = "https://realpython.github.io/fake-jobs/"
page = requests.get(res)
#print(page.text)
#print(page.content) # raw bytes, jota parempi käyttää koska character encode?
print(page.ok)

if not page.ok:
    print('Could not load the page')
    sys.exit

soup = BeautifulSoup(page.content, "html.parser")

jobs = soup.find_all(class_='card')
job_count = 0

for job in jobs:
    location = job.find(class_='location')
    state = location.text.split(',')[1].strip() # split pilkusta ja napataan osavaltio [indeksi=1]
    if state == 'AE':
        title = job.find('h2', class_='title').text
        link = job.find(text='Apply').parent['href']
        print(f'Title: {title}\nLocation: {location}\nApply here: {link}\n\n')
        job_count += 1

print(f'Jobeja on: {job_count}')
