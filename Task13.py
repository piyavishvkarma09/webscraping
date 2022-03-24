import json
from Task5 import movie_list
from Task1 import a
from Task_12 import scrape_movie_cast

def  casting_list():
    newlist=[]
    for i in range(10):
        newlist.append(movie_list[i])

    for i in range(10):
        url=a[i]["Movie URL"]
        sd=scrape_movie_cast(url)
        newlist[i]["cast"]=sd
    with open("task13.json","w")as file1:
         json.dump(sd,file1,indent=4)  
    return newlist 

casting=casting_list()