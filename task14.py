import json
def startswith_A(file1,file2):
      with open(file1,'r') as f,open(file2,'w') as d:
            data=json.loads(f.read())
            lst=[]
            for i in data:
                  if str(i['name']).startswith('A' or'a'):
                        lst.append(i['name'])
            d.write(json.dumps({'a_names':lst},indent=4))
startswith_A('Input/students.json','Output/output14.json')