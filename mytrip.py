from bs4 import BeautifulSoup
import requests
import re
page = requests.get('http://bus.com.ua/cgi-bin/tablo.pl')
class bigparsing:
        def all_parsing(page):
                soup = BeautifulSoup(page.text, 'html.parser')
                name = soup.find_all('a')
                myregex = re.compile('<a href="tablo.pl\?as=\d{6}">')
                mydict = {}
                for i in name:
                        if re.match(myregex, str(i)):
                                i = str(i)
                                i = i.replace('</a>', "")
                                formydict = re.split('>',i)
                                mydict[formydict[0]] = formydict[1]
                
                return mydict

