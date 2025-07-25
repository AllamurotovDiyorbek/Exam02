def  nine(file1,file2):
    with open(file1,"r") as f, open(file2, "w") as s:
        c=0
        for i in f.readlines():
            if c<int(i):
                c=int(i)
        s.write(f"Eng katta son: {str(c)}")
nine("Input/numbers.txt","Output/output09.txt")