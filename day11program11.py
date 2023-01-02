sample_dict= {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"}
keys=["name","salary"]

newDict={}
for i in keys:
    newDict[i]=sample_dict[i]
print(newDict)


newDict={ i:sample_dict[i] for i in keys }
print(newDict)


res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
