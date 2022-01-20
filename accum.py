#accum

def accum(s):
    inicio=[]
    ciclo=1
    lista=[]
    for i in s:        
        lista.append(i)
        lista[ciclo-1]=lista[ciclo-1]*ciclo
        lista[ciclo-1]=str(lista[ciclo-1]).title()
        ciclo+=1        
    return ("-").join(lista)
print(accum("holas"))
