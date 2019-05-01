from bs4 import BeautifulSoup
import requests
import re

page = requests.get('http://bus.com.ua/cgi-bin/bus-order?b=050700&r=185%E0')
soup = BeautifulSoup(page.text, 'html.parser')
name = soup.find_all('tr')
myregex0 = re.compile('<a href="http://bus.com.ua/cgi-bin/poshuk\?\w\w=\d\d\d\d\d\d&amp;\w\w=\d\d\d\d\d\d&amp;\w\w=\d\d\d\d\d\d">')

for i in name:
    if re.match('<tr bgcolor="#e0f0f0"', str(i)) or re.match('<tr bgcolor="#e7f7f7', str(i)):
        i = str(i)
        i = i.replace('<tr bgcolor="#e0f0f0"><td> </td><td>', '')
        i = i.replace('<tr bgcolor="#e7f7f7"><td>', '')
        i = i.replace(' </td><td>', ';')
        i = i.replace('<tr bgcolor="#e0f0f0"><td>', '')
        i = i.replace('</a></td><td> ', ';')
        i = i.replace('</td><td> ', ';')
        i = i.replace('</td></tr>', '')
        i = i.replace('<i><b>', '')
        i = i.replace('</b></i></td><td>', '')
        i = re.sub(myregex0, "", i)
        print(str(i))
