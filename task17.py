numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]
d=[]
d=list(filter(lambda user:user['value']>0,numbers))
print(d)