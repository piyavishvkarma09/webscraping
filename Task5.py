from bs4 import BeautifulSoup
import json
from Task1 import a
from Task4 import scrape_movie_details

def get_movie_list_details(movies):
    mylist=[]
    # detail_list=[]
    for j in movies:
        mylist.append(j)
    # print(mylist)
    url_namelist={}
    
    for j in mylist:
        url_namelist.update({j["link"]:j["Movie Name"]})
    # print(url_namelist)

    detail_list=[]
    for link,name in url_namelist.items():
        b=scrape_movie_details(link,name)
        detail_list.append(b)
    with open ("movie_url.json","w") as file:
        json.dump(detail_list,file, indent=4)
    return  detail_list

movie_list=(get_movie_list_details(a))