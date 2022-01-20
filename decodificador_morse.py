#decocder morse 

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    a=".-"
    b="-..."
    c="-.-."
    d="-.."
    e="."
    f="..-."
    g="--."
    h="...."
    i=".."
    j=".---"
    k="-.-"
    l=".-.."
    m="--"
    n="-."
    o="---"
    p=".--."
    q="--.-"
    r=".-."
    s="..."
    t="-"
    u="..-"
    v="...-"
    w=".--"
    x="-..-"
    y="-.--"
    z="--.."
    punto=".-.-.-"
    exclamacion="-.-.--"
    letras="ABCDEFGHIJKLMNOPQRSTUVWXYZ.!"
    mensaje=[]    
    morse_chain=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".-.-.-","-.-.--"]
    morse_code=morse_code.replace("   "," * ")
    partidor=morse_code.split(" ")       
    for i in partidor :
        signo=0
        if i=="*":
            mensaje.append(" ")
        elif i=="...---...":
            mensaje.append("SOS")
        for k in morse_chain:
            if k==i:
                mensaje.append(letras[signo])
            signo+=1  
    print(mensaje)
    mensaje=("").join(mensaje) 
    mensaje=mensaje.strip()
    print("el original :\n",morse_code)
    print("el mensaje traducido es :\n",mensaje)    
    return mensaje
decodeMorse('  *  * ...---... -.-.-- * - .... . * --.- ..- .. -.-. -.- * -... .-. --- .-- -. * ..-. --- -..- * .--- ..- -- .--. ... * --- ...- . .-. * - .... . * .-.. .- --.. -.-- * -.. --- --. .-.-.- ')
decodeMorse("     .    .")


    
'''
# como debe ser
    decodeMorse('.... . -.--   .--- ..- -.. .')
    #should return "HEY JUDE"


   return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
'''
























##
##def test_and_print(got, expected):
##    if got == expected:
##        test.expect(True)
##    else:
##        print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
##        test.expect(False)
##
###test.describe("Example from description")
##print(test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE'))
##
###test.describe("Your own tests")
# Add more tests here
