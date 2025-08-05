import csv
def status_s(file1,file2):
      with open(file1,'r') as f,open(file2,'w') as d:
            data=csv.DictReader(f)
            next(data)
            mx=0
            for i in data:
                  c=int(i['grade'])
                  if c>mx:
                        mx=c
                        name=i['name']
            d.write(f"Bahosi eng yuqori o`quvchi: {name} - {mx}")
status_s('Input/grades.csv','Output/output15.txt')