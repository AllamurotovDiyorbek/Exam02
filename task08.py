def  eight_task(file1,file2):
    with open(file1,"r") as f, open(file2, "w") as s:
        c=0
        for i in f.readlines():
            c+=int(i)
        s.write(str(c))
eight_task("Input/numbers.txt","Output/output08.txt")