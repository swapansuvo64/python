x=int(input("Enter Number: "))
def fact(x):
    pro=1
    for i in range (1,x+1):
        pro*=i
    return pro
def factreq(x):
    pro=1
    if x==1:
        return 1
    pro=pro*x*factreq(x-1)
    return pro
pro=factreq(x)
pro1=fact(x)
print(pro,pro1)
