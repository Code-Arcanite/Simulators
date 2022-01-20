#pig latin

def pig_it(text):
    #your code here
    partidor=text.split(" ")
    pig_latin=[]
    for i in partidor:
        if i.isalpha():
            inicial=str(i[0])
            resto=str(i[1:])
            total=resto+inicial+"ay"
            pig_latin.append(total)
        else:
            pig_latin.append(i)
    return " ".join(pig_latin)

print(pig_it('Pig latin is cool'))









##pig_it('Pig latin is cool') # igPay atinlay siay oolcay
##pig_it('Hello world !')     # elloHay orldway !
