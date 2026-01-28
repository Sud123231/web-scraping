from bs4 import BeautifulSoup
import requests

#overview of scrapping
with open('home.html','r') as content:
    a=content.read()
    soup=BeautifulSoup(a,'lxml')
    output=soup.find_all('strong')# this returns list of tags or whatever we search for
    #for item in output:
    print(output.text) #or print(item.h5.text) if we want only text of h5 tags inside item       


