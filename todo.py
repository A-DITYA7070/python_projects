import json

user=input("enter your id ")
with open(f"{user}.json","w+") as f:
    data={}
    json.dump(data,f,indent=0)
    