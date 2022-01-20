#area of squares

def perimeter(n):
    # your code
    long_d=1
    long_a=1
    area=0
    fibbonaci=[]
    for i in range(n):
        fibbonaci.append(long_a)
        long_a+=long_d
        long_d=fibbonaci[-1]
    return (sum(fibbonaci)+1)*4
print(perimeter(7))
        





##perimeter(5)  should return 80
##perimeter(7)  should return 216
