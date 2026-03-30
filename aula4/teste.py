import random

copo1= random.randint(1,4)
copo2= random.randint(1,4)
while copo2==copo1:
    copo2= random.randint(1,4)
copo3= random.randint(1,4)
while copo3 == copo2 or copo1:
    copo3 = random.randint(1,4)
copo4= random.randint(1,4)
while copo4 == copo2 or copo1 or copo3:
    copo4 = random.randint(1,4)
 