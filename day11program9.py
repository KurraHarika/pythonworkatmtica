employees=['Kelly', 'Emma']
defaults={"designation": 'Developer', "salary": 80000}

data=dict.fromkeys(employees,defaults)
print(data)
print(data["Emma"])
