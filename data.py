from bs4 import BeautifulSoup as b
import requests as req
def scrap(link):
    file=req.get(link)
    if(file.ok):
        content=b(file.text,'html.parser')
        tags=content.find_all('p')
        with open('document.txt','w') as cleardoc:
            cleardoc.write('')
        for tag in tags:
            try:
                with open('document.txt','a') as doc:
                    doc.write(tag.text)
            except:
                continue
        return True
    else:
        return False