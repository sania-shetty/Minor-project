from bs4 import BeautifulSoup as b
import requests as req
def scrap():
    file=req.get("https://en.wikipedia.org/wiki/Virat_Kohli").text
    content=b(file,'html.parser')
    tags=content.find_all('p')
    for tag in tags:
        try:
            with open('sample2.txt','a') as doc:
                doc.write(tag.text)
        except:
            continue