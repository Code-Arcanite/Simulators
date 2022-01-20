#raiz digital

def digital_root(n):
    if n<10:
        return int(n)
    n=str(n) 
    lista=[]
    n_k=list(n)
    for i in n_k:
        lista.append(int(i))
    suma_n=0
    while len(lista)!=1:
        suma_n=sum(lista)
        lista=[]
        suma_n=str(suma_n)
        for m in suma_n:
            lista.append(int(m))        
    return int(suma_n)

print(digital_root(11))

'''
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

Test.assert_equals(digital_root(16), 7)
Test.assert_equals(digital_root(942), 6)
Test.assert_equals(digital_root(132189), 6)
Test.assert_equals(digital_root(493193), 2)
'''
