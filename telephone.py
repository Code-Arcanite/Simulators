#telephone

##Write a function that accepts an array of 10 integers (between 0 and 9),
##that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    #your code here
    numero1=str(n[:3])
    numero2=str(n[3:6])
    numero3=str(n[6:])
    numero1=numero1.replace(",","")
    numero1=numero1.replace("[","")
    numero1=numero1.replace("]","")
    numero1=numero1.replace(" ","")
    numero2=numero2.replace(",","")
    numero2=numero2.replace("[","")
    numero2=numero2.replace("]","")
    numero2=numero2.replace(" ","")
    numero3=numero3.replace(",","")
    numero3=numero3.replace("[","")
    numero3=numero3.replace("]","")
    numero3=numero3.replace(" ","")
    real='('+numero1+') '+numero2+'-'+numero3+')'
    return real
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



'''
##assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
"(123) 456-7890")
##assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
"(111) 111-1111")
##assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
"(123) 456-7890")
'''
