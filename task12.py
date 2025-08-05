import json
with open("Input/students.json","r") as f:
    content=f.read()
    data=json.loads(content)
    c=[]
    for i in data:
        c.append(i['name'])
        
with open("Output/output11.json","w") as h:
    jso=json.dumps({"count":len(data)},indent=3)
    h.write(json)