import json
import requests
from bs4 import BeautifulSoup
import os
from Task1 import a


def scrape_movie_cast (url):
    castname=[]
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    tag=soup.find("div",class_="castSection")

    allcast=tag.find_all("div",class_="cast-item media inlineBlock")
    for cast in allcast:

        link2=cast.find("a",class_="unstyled articleLink")
        name=cast.find("span").get_text().strip()
        # print(name)
        link=link2["href"]
        # crew_link="https://www.rottentomatoes.com"+link
    
    
        mydic={}
        mydic.update({"name":name})
        mydic.update({"link":link})

        castname.append(mydic)
    with open("cast_name.json","w")as k:
        json.dump(castname,k,indent=4)

    return castname
url=a[0]["link"]
scrape_movie_cast(url)