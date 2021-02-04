from random import randint, choice

testlist = ("Chocobo", "Moogle", "Poro", "Kuriboh")

cute = "Moogle"

if cute in testlist:
    print(cute, ' is cute')
"""
STR = 9
DEX = 14
COS = 11
INT = 15
WIS = 12
CAR = 11
Statlist1 = [STR, DEX, COS, WIS, INT, CAR]
Statlist2 = [STR, DEX, COS, WIS, INT, CAR]

for n, i in enumerate(Statlist1):
    temp1 = choice(Statlist1)
    print(temp1)
    if temp1 in Statlist2:
        Statlist1[n] = temp1+1
print(Statlist1)
"""
"""
if 14 in Statlist1:
    for x in range(2):
        int1 = randint(1, 6)
        if int1 == 1:
            STR = STR + 1
        elif int1 == 2:
            DEX = DEX + 1
        elif int1 == 3:
            COS = COS + 1
        elif int1 == 4:
            WIS = WIS + 1
        elif int1 == 5:
            INT = INT + 1
        elif int1 == 6:
            CAR = CAR + 1

print(Statlist1)
temp1 = choice(Statlist1)

print(temp1)
Statlist2.remove(temp1)
print(Statlist2)
temp2 = choice(Statlist2)
"""

randnum1 = randint(1, 6)
randnum2 = randint(1, 6)
if randnum2 == randnum1:
    print("Num2 is: " + str(randnum2) + "changeing to: ")
    randnum2 = randint(1, 6)

print(randnum2)
print(randnum1)





