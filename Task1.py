from bs4 import BeautifulSoup
import requests
# import pprint #(to prettify print)
import json
def scrape_top_list():

    link=("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
    url=requests.get(link)
    Beautiful_soup=BeautifulSoup(url.text,'html.parser')
    main_container=Beautiful_soup.find("table",class_="table")
    sub_container=main_container.find_all("tr")
    movie_list=[]
    for i in sub_container[1:]:
        movie_rank=i.find("td",class_="bold")
        rank=(movie_rank.get_text())#strip()with text

        movie_ratings=i.find("span", class_="tMeterScore")#to print(ratings)
        rating=(movie_ratings.get_text())

        movie_title=i.find("a" ,class_="unstyled articleLink")#movie name
        title= movie_title.get_text()

        list=title.split()
        year=list[-1][1:5]
        real_year=int(year)
        name_lenght=len(list)-1
        name=" "
        for j in range(name_lenght):
            name+=" "
            name+=list[j]

        movie_Name=name
        movie_Reviews=i.find("td",class_="right hidden-xs")
        reviews=movie_Reviews.get_text()

        url=i.find("a",class_="unstyled articleLink")
        link=url["href"]
        movie_Link="https://www.rottentomatoes.com"+link

        details={}
        details["Movie Name"]=movie_Name
        details["Movie Rank"]=rank
        details["Movie Revies"]=rating
        details["Movie Revies"]=reviews
        details["year"]=real_year
        details["link"]=movie_Link
        movie_list.append(details)
    # print(movie_list)
    with open("movie_list.json","w") as file:
        json.dump(movie_list,file,indent=3)
    return movie_list
# print()

a=scrape_top_list()



            