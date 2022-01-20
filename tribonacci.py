#tribbonaci

def tribonacci(assignature,n):
    uno=assignature[0]
    dos=assignature[1]
    tres=assignature[2]
    lista=[]
    lista.append(uno)
    lista.append(dos)
    lista.append(tres)
    A=0

    if n==3:

        return lista
    if n==2:

        lista_2=lista[:2]
        return lista_2 
    if n==1:

        lista_1=lista[:1]
        return lista_1
    if n==0:
        lista_0=[]
        return lista_0
              
    while len(lista)<n:
        i=0
        cuatro=lista[i+A]+lista[i+A+1]+lista[i+A+2]
        lista.append(cuatro)
        A+=1

    return lista
    
#Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
##    string=[]
##    k=0
##    while len(string)<=n:
##        if k==0:
##            for i in assignature:
##                print(i)
##                string.append(i)
##        string.append((string[0+k]+(string[1+k]+(string[2+k]))))
##        k+=1
print(tribonacci([3,2,1],1))
#Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
#Test.assert_equals(tribonacci([300, 200, 100], 0), [])
   
        



#Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
