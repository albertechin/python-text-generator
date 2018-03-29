import random
import string

vow = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"
ltr = string.ascii_lowercase

ltr1_typ = input("Enter v | l | c: ")
ltr2_typ = input("Enter v | l | c: ")
ltr3_typ = input("Enter v | l | c: ")

def genx():
    if ltr1_typ == 'v':
        ltr1 = random.choice(vow)
    elif ltr1_typ == 'c':
        ltr1 = random.choice(cons)
    elif ltr1_typ == 'l':
        ltr1 = random.choice(ltr)
    else:
        ltr1 = ltr1_typ

    if ltr2_typ == 'v':
        ltr2 = random.choice(vow)
    elif ltr2_typ == 'c':
        ltr2 = random.choice(cons)
    elif ltr2_typ == 'l':
        ltr2 = random.choice(ltr)
    else:
        ltr2 = ltr2_typ


    if ltr3_typ == 'v':
        ltr3 = random.choice(vow)
    elif ltr3_typ == 'c':
        ltr3 = random.choice(cons)
    elif ltr3_typ == 'l':
        ltr3 = random.choice(ltr)
    else:
        ltr3 = ltr3_typ

    txt = ltr1 + ltr2 + ltr3
    print(txt)

for i in range(10):    
    genx()