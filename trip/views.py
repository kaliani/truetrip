from django.shortcuts import render, render_to_response
from django.http import HttpResponse
#from . import bigparsing
from bs4 import BeautifulSoup
import requests
import re

def mainmytrip(request):
    #return HttpResponse('Hello world!')
    page = requests.get('http://bus.com.ua/cgi-bin/tablo.pl')
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
    return render_to_response('all_trip.html', {'data': sorted(mydict.items())})