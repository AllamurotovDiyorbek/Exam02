def calculator(son1:int,son2:int,amal:str):
    natija=0
    if amal in ["*","/","+","-"]:
        if amal=="*":
            natija=son1*son2
        elif amal=="/":
            natija=son1/son2
        elif amal=="+":
            natija=son1+son2
        elif amal=="-":
            natija=son1-son2
        return f'{son1}{amal}{son2}={natija}'
    else:
        return "Amal faqat: -,+,*,/ "
son1=int(input("SON1: "))
son2=int(input("SON2: "))
print("Amal faqat: -,+,*,/ ")
amal=input("Amal:")
calculate=calculator(son1,son2,amal)
print(calculate)