def text(text):
    dct={}
    text=text.split(" ")
    for i in range(len(text)):
        dct[text[i]]=text.count(text[i])
    return dct
print(text("Salom Salom Doniyor"))