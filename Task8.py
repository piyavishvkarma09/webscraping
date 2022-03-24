import json
from Task1 import a
import os
from Task4 import scrape_movie_details
from functools import lru_cache
lru_cache (maxsize=1000)
def scrape_new_movie_details(url2):
    # print(url2)
    for i in a:
        if i["link"]==url2:
            url=i["link"][33:]
            # print(url)
            url1=i["link"]
            name=i["Movie Name"]
    filename="/home/piyavishvkarma/Desktop/web scraping/"+url+".json" 
    # print(filename)
       
    file=os.path.exists(filename)
    print(file)
    if file==True:
        print(" it is exists")
        with open(filename,"r")as m:
            details=json.load(m)
            print(details)
    else:
        print("it is not exists")
        data=scrape_movie_details(url1,name)   
        print(data)

        with open(filename,"w") as file:
            json.dump(data,file,indent=4)
        print(filename)

url2=a[1]["link"]
print(url2)
       
scrape_new_movie_details(url2)