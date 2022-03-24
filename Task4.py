from urllib import response
from Task1 import a
import requests
import json 
from bs4 import BeautifulSoup


def scrape_movie_details(movie_url,name):
    url=(movie_url)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    movie_tags=soup.find("ul",class_="content-meta info")
    sub=movie_tags.find_all("li",class_="meta-row clearfix")
    
    dict_details={}
    dict_details["name"]=name
    for i in sub:

        key=i.find("div",class_="meta-label subtle").text.strip()
        values=(i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip())
        dict_details[key]=values
    
                
    with open("movie_details.json","w")as file:
        json.dump(dict_details,file,indent=4)
    # print(dict_details)
    return dict_details
    

for i in a:
    url_link=a[0]["link"]
    name=a[0]["Movie Name"]
# print(response)
# print(url_link,name)

scrape_movie_details(url_link,name)
    