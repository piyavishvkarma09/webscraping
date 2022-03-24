from requests import models
from task2 import a
import requests
import json 
from bs4 import BeautifulSoup

def group_by_decade(movie):
    movie_Decade={}
    list=[]
    for i in movie:
        mode=i%10
        Decade= i-mode
        if Decade not in list:
            list.append(Decade)
    list.sort()
    # print(list)
    for i in list:
        movie_Decade[i]=[]
    for i in  movie_Decade:
        decd=i+9
        for x in movie:
            if x<=decd and x>=i:
                for v in movie[x]:
                    movie_Decade[i].append(v)
    with open("group_by_decade.json","w") as file:
        json.dump(movie_Decade,file,indent=4)
    # print(movie_Decade)
    return (movie_Decade)

group_by_decade(a)