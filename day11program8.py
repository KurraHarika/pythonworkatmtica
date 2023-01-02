employees=['Kelly', 'Emma']
defaults={"designation": 'Developer', "salary": 80000}

data=dict()
for i in employees:
    data[i]=defaults
print(data)
