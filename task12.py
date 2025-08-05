import json
with open("Input/students.json","r") as f,open("Output/output12.json","w") as h:
    content=f.read()
    data=json.loads(content)
    sort_name=[]
    for i in data:
        sort_name.append(i['name'])
    sort_name.sort()
    h.write(json.dumps({"sorted_names":sort_name},indent=4))
