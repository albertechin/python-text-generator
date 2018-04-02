import string
import random

psw = string.printable

def genx_text(l): 
    gen = ""

    for i in range(l):
        gen += random.choice(psw)
    
    return gen


#Test
l = int(input("Enter the length of the psw to be generated: "))

psw_gen = genx_text(l)
print("Generated Password: {}".format(psw_gen))


