from Task5 import movie_list
import json

def analyse_movies_language (movie_list):
    language={}
    for i in movie_list:
        count=0
        for j in movie_list:
            if i["Original Language:"]==j["Original Language:"]:
                count=count+1
            language.update({i["Original Language:"]:count})
        # print(language)

    
    with open("language.json","w")as file:
        json.dump(language,file,indent=4)
    return language 

analyse_movies_language (movie_list)

