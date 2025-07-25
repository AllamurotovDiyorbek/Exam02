def diller(students):
  c=0
  t=0
  g=0
  for i in students.values():
    c+=i
    t+=1
  g=round(c/t,2)
  d=""
  for i,f in enumerate(students):
    if i>g:
      if f!="":
        d+=","
      d+=c
  return d
students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
h=diller(students)
print(h)