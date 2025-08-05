import csv
def baho(file1,file2):
      with open(file1,'r') as f,open(file2,'w') as d:
            data=csv.reader(f)
            next(data)
            c=0
            for i in data:
                  if (i[1])=='5':
                        c+=1
            d.write(f'5 baha olganlar soni {c}')
baho('Input/grades.csv','Output/output16.txt')
