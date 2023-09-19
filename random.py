import random
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
for roll in range (1,6001):
    face=random.randrange(1,7)
    if face is 1:
        f1+=1
    elif face is 2:
        f2+=1
    elif face is 3:
        f3+=1
    elif face is 4:
        f4+=1
    elif face is 5:
        f5+=1
    elif face is 6:
        f6+=1
print("1%13d"%f1)
print("2%13d"%f2)
print("3%13d"%f3)
print("4%13d"%f4)
print("5%13d"%f5)
print("6%13d"%f6)
