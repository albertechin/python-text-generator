import random
import string

vow = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"
ltrs = string.ascii_lowercase

ltr1_typ = input("Enter v | l | c: ")
ltr2_typ = input("Enter v | l | c: ")
ltr3_typ = input("Enter v | l | c: ")

def genx_ltr(ltr_typ):
    if ltr_typ == 'v':
        ltr = random.choice(vow)
    elif ltr_typ == 'c':
        ltr = random.choice(cons)
    elif ltr_typ == 'l':
        ltr = random.choice(ltrs)
    else:
        ltr = ltr_typ

    return ltr

def genx_text():
    ltr1 = genx_ltr(ltr1_typ)
    ltr2 = genx_ltr(ltr2_typ)
    ltr3 = genx_ltr(ltr3_typ)

    txt = ltr1 + ltr2 + ltr3
    print(txt)

for i in range(10):    
    genx_text()