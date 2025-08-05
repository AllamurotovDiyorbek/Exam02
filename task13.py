import json
with open("Input/students.json","r") as f:
    content=f.read()
    data=json.loads(content)
    for i in data:
with open("Output/output13.json","w") as h:
    jso=json.dumps({"count":len(data)},indent=3)
    h.write(jso)