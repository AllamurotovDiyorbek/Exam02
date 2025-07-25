def calculator(son1:int,son2:int,amal:str):
    natija=0
    if amal in ["*","/","+","-"]:
        if amal=="*":
            natija=soni*son2
        elif amal=="/":
            natija=soni/son2
        elif amal=="+":
            natija=son1+son2
        elif amal=="-":
            natija=son1-son2
        print(natija)
    else:
        print("Amal faqat: -,+,*,/ ")
calculator(int(input("SON1 ")),int(input("SON2 ")),input("Amal: "))