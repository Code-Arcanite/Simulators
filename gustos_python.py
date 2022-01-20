def likes(names):
    # your code here
    response=""
    if names==None or names=="":
        return ("no one likes this")
    elif len(names)==1:
        return names[0]+" like this"
    elif len(names)==2:
 
        response=names[0]+" and "+names[1]+" like this"
        return response
    elif len(names)==3:
        response=names[0]+", "+names[1]+" and "+names[2]+" like this"
        return response
    elif len(names)>3:
        long=len(names)
        response+=names[0]+", "+names[1]+" and "+str(long-2)+" others like this"
        return response
        


    #return response
    #respuesta=
            
    #return
print(likes(["Alex", "Jacob", "Mark", "Max"]))

"""
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""
