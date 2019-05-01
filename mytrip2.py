from bs4 import BeautifulSoup
import requests
import re
lst = []
page = requests.get('http://bus.com.ua/cgi-bin/tablo.pl?as=050700')
soup = BeautifulSoup(page.text, 'html.parser')
name = soup.find_all('tr')
regextemplate = re.compile('<br/>  -  <a href="bus-order\?b=\d{6}&amp;r=\w{1,10}"><font style="font-size:100%;"><b>') 
for i in name:
    if re.match('<tr bgcolor="#f2f9f9"', str(i)):
            i = str(i)
            i = i.replace('<tr bgcolor="#f2f9f9"><td align="right" style="font-size:120%;"><b>', "")
            i = i.replace('</b><br/><font style="font-size:80%;">', ";")
            i = i.replace('</font></td><td align="left" style="font-size:110%;">', ";")
            i = i.replace('</b></font></a></td></tr>', "")
            i = re.sub(regextemplate,"", i)
            print(str(i))

