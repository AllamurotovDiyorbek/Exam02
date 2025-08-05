students = [
    {'name': 'Ali', 'age': 28},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
def min_name(students):
    c=[]
    for i in students:
        c.append(i['name'])
    c=min(c)
    return c
print(min_name(students))