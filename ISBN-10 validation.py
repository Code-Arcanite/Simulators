#validacion de ISBN-10



def valid_ISBN10(isbn): 
    # your code here
    numeros=[]
    suma=[]
    if len(isbn)==10:
        numeros=list(isbn)
#        print(numeros)
        A=1
        for k in numeros:
            if k.isdigit():
                suma.append(A)
                suma[-1]=int(k)*A
           
            if A==10 and k.upper()=="X":
                suma.append(100)
         
            A+=1                 

        print("la lista suma es :",suma)
        print("isbn completo =",sum(suma))
        if len(suma)==0:
            return False
        if sum(suma)%11==0:
            return True
        else:
            return False
        print(numeros)
    else:   
        return False


print(valid_ISBN10('048665088X'))



'''
@test.it("Sample tests")
def tests():
    test.assert_equals(valid_ISBN10('1112223339'), True)
    test.assert_equals(valid_ISBN10('048665088X'), True)
    test.assert_equals(valid_ISBN10('1293000000'), True)
    test.assert_equals(valid_ISBN10('1234554321'), True)
    test.assert_equals(valid_ISBN10('1234512345'), False)
    test.assert_equals(valid_ISBN10('1293'), False)
    test.assert_equals(valid_ISBN10('X123456788'), False)
    test.assert_equals(valid_ISBN10('ABCDEFGHIJ'), False)
    test.assert_equals(valid_ISBN10('XXXXXXXXXX'), False)
    ISBN     : 1 1 1 2 2 2 3 3 3  9
    position : 1 2 3 4 5 6 7 8 9 10
    (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0


'''
