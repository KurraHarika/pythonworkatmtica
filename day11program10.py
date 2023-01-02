sample_dict= {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"}
keys=["name","salary"]

newDict={k: sample_dict[k] for k in keys}
print(newDict)
             
