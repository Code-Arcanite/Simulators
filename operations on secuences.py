#escalera 

def solve(arr):
    # your code
    m=0
    g=0
    L=0
    lista=[]
    while L<=len(arr):

        A=arr[L]
        B=arr[L+1]
        print(lista)
        if L%2==0:
            A_m=A*A
            B_m=B*B
            lista.append(A_m+B_m)
        
        L+=1      
    return j
solve([2, 1, 3, 4])





'''
solve([2, 1, 3, 4]) returns [2, 11] :
(2*2 + 1*1) * (3*3 + 4*4) = 5 * 25 = 125 -->
--> and 2 * 2 + 11 * 11 = 125

solve([2, 1, 3, 4, 2, 2, 1, 5, 2, 3, 4, 5]) returns
[2344, 2892] :
(2*2 + 1*1) * (3*3 + 4*4) * (2*2 + 2*2) * -->
--> (1*1 + 5*5) * (2*2 + 3*3) * (4*4 + 5*5) = 13858000
and 2344 * 2344 + 2892 * 2892 = 13858000




'''
