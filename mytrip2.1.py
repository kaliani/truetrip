from bs4 import BeautifulSoup
import requests
import re

page = requests.get('http://bus.com.ua/cgi-bin/tablo.pl?as=050700')
soup = BeautifulSoup(page.text, 'html.parser')
name = soup.find_all('tr')

myregex0 = re.compile('<tr bgcolor="#f2f9f9"><td align="right" style="font-size:120%;"><b>.....') 
'''
myregex0 = re.compile('<tr bgcolor="#f2f9f9"><td align="right" style="font-size:120%;"><b>.....</b><br/><font style="font-size:80%;">........</font></td><td align="left" style="font-size:110%;">.........<br/>  -  ')
myregex = re.compile('<br/>  -  <a href="bus-order\?b=\d\d\d\d\d\d&amp;r=\w\w\w">')
myregex1 = re.compile('<br/>  -  <a href="bus-order\?b=\d\d\d\d\d\d&amp;r=\w\w\w\w">')
myregex2 = re.compile('<br/>  -  <a href="bus-order\?b=\d\d\d\d\d\d&amp;r=\w\w\w\w\w">')
myregex3 = re.compile('><font style="font-size:100%;"><b>')  '''
for i in name:
    if re.match('<tr bgcolor="#f2f9f9"', str(i)):
        i = str(i)
        #i = i.replace()
        i = re.sub(myregex0,"",i)
        print(str(i))


