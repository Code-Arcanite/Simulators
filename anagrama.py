#anagrama

def anagrams(word, wordA):
    #your code here
    real=[]
    for words in wordA:
        longA=len(word)
        longB=len(words)
        if longA!=longB:
            pass
        else:            
            ponts=0
            for i in words:                
                if i in word:
                    ponts+=1

            for i in word:                
                if i in words:
                    ponts+=1
                if i not in words:
                    ponts-=10
            if ponts==longA*2:
                real.append(words)
    return real

print(anagrams('racer',['crazer', 'carer', 'racar', 'caers', 'racer']))


"""
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer']

"""
