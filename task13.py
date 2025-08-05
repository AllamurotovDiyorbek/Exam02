import json
with open("Input/students.json","r") as f,open("Output/output13.json","w") as h:
    content=f.read()
    data=json.loads(content)
    lst=[]
    for i in data:
        if len(i['name'])>5:
            lst.append(i['name'])
    h.write(json.dumps({'long_names':lst},indent=4))