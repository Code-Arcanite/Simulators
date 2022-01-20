#alphabet war



def alphabet_war(battlefield):
    lugar=0
    bombardeo=[]
    bunkeres=[]
    afuera=[]
    salvo=[]
    L=0
    for i in battlefield:

        if i=="#":
            bombardeo.append(lugar)
        lugar+=1
        if i=="[" or i=="]":
            bunkeres.append(lugar)
    huecos=(len(bunkeres))/2
    print("bunkeres a salvo :",int(huecos))
    A=0
    for k in range(len(bunkeres)-1):            
        salvo.append(battlefield[bunkeres[A]:bunkeres[(A+1)]])
        print(salvo)
        A+=1
    print("las letras que estan a salvo son :",salvo)
    print("bombardeos en ubicaciones :",bombardeo)
    
    return "oops"

alphabet_war("##abde[fgh]ijk[mn]op")



'''
abde[fgh]ijk     => "abdefghijk"  (all letters survive because there is no # )
ab#de[fgh]ijk    => "fgh" (all letters outside die because there is a # )
ab#de[fgh]ij#k   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#ab#de[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#abde[fgh]i#jk[mn]op => "mn" (letters from the second shelter survive, there is only 1 # close)
[a]#[b]#[c]  => "ac"
[a]#b#[c][d] => "d"
[a][b][c]    => "abc"
##a[a]b[c]#  => "c"
'''
