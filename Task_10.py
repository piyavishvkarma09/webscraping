import json
from Task5 import movie_list

new_dic={}
for i in movie_list:
    count=0
    for j in movie_list:
        if i["Director:"]==j["Director:"]:
            if i["Original Language:"]==j["Original Language:"]:
                count=count+1
        new_dic.update({i["Director:"]:{i["Original Language:"]:count}})

with open("task10.json","w")as file:
    json.dump(new_dic,file,indent=4)
