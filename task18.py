numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
t=[]
for i in numbers:
    t.append({'value':i['value']**2})
print(t)