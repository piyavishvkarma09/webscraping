from Task5 import movie_list
import json

def analyse_movies_directors(movie_list):
    director_list={}
    for i in movie_list:
        count=0
        for j in movie_list:
            if i["Director:"]==j["Director:"]:
                count=count+1
        director_list.update({i["Director:"]:count})
    # print(director_list)


    with open("director.json","w")as file:
        json.dump(director_list,file,indent=4)


analyse_movies_directors(movie_list)