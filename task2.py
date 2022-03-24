from Task1 import scrape_top_list
import requests
import json 
from bs4 import BeautifulSoup

task1=scrape_top_list()
def group_by_year(movie):
    years=[ ]
    for i in movie:
        year= i["year"]
        # print(years)
        if year not in years:
            years.append(year)
    # print(years)
    movie_dict={i:[]for i in years}
    for i in movie:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("group_by_year.json","w") as file:
        json.dump(movie_dict,file,indent=3)
    return movie_dict
a=group_by_year(task1)
# print(a)

































# for i in (5,50,1):
#     print(5,"*",1,"=",5*1)


# a=int(input("enter the number"))
# i=1
# while(i<=10):
#     print(a,"*",i,"=",a*i)
#     i=i+1

# i=1
# a=1
# while(i<=5):
#     j=1
#     while(j<=5):
#         print(j*i,end=" ")
#         j=j+1
#     a=a+2
#     print()
#     i=i+1