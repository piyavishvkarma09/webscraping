import json
from Task5 import movie_list

def analyse_movies_genre():
    gener_list=[]
    for i in movie_list:
        gener_split=i["Genre:"].split(",")
        for j in gener_split:
            gener_list.append(j)
    # print(gener_list)

    gener_dic={}
    for gener in gener_list:
        count=0
        for gener_con in gener_list:
            if gener==gener_con:
                count=count+1
            gener_dic.update({gener:count})
    # print(gener_dic)
    with open("analyse_gener.json","w")as generfile:
        json.dump(gener_dic,generfile,indent=4)
    return gener_dic
    
analyse_movies_genre()




