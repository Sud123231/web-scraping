from bs4 import BeautifulSoup
import requests

# #overview of scrapping
# with open('home.html','r') as content:
#     a=content.read()
#     soup=BeautifulSoup(a,'lxml')
#     output=soup.find_all('strong')# this returns list of tags or whatever we search for
#     #for item in output:
#     print(output.text) #or print(item.h5.text) if we want only text of h5 tags inside item       

html_text=requests.get("https://quotes.toscrape.com/").text
soup=BeautifulSoup(html_text,'lxml')
content=soup.find_all('div',class_="quote")
with open('quotes.txt','w',encoding="utf-8") as f:
    f.write('Index, Author, Quote\n')
    for (idx,item) in enumerate(content):
        author=item.find('small', class_='author').text
        quote=item.span.text
        f.write(f'{idx}, {author}, {quote}\n')
