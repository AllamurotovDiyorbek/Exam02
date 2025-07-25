def ten(file1,file2):
    with open(file1,"r") as f, open(file2, "w") as s:
        c=[]
        for i in f.readlines():
            c.append(int(i))
        c.sort()
        for a in c:
            s.writelines(f"{str(a)}\n")
ten("Input/numbers.txt","Output/output10.txt")