import random
import string

vow = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"
ltr = string.ascii_lowercase

ltr1 = random.choice(vow)
ltr2 = random.choice(cons)
ltr3 = random.choice(ltr)

txt = ltr1 + ltr2 + ltr3

print(txt)
