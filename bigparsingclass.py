from bs4 import BeautifulSoup
import requests
import re
page = requests.get('http://bus.com.ua/cgi-bin/tablo.pl')
class bigparsing:
        def parsing_main_page(city):
                soup = BeautifulSoup(page.text, 'html.parser')
                name = soup.find_all('a')
                myregex = re.compile('<a href="tablo.pl\?as=\d{6}">')
                mydict = {}
                for i in name:
                        if re.match(myregex, str(i)):
                                i = str(i)
                                i = i.replace('</a>', "")
                                i = i.replace('<a href="tablo.pl?as=', "")
                                i = i.replace('"', "")
                                formydict = re.split('>',i)
                                mydict[formydict[1]] = formydict[0]
                return mydict[city]
        print(parsing_main_page('УЖГОРОД 2'))
#print(mydict.get('УЖГОРОД 2'))
