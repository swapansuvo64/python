a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a is b and b is c and c is a:
    print("All equal")
elif a>b and a>c:
    print(a,"is greate")
elif b>a and b>c:
    print(b,"is greater")
elif c>a and c>b:
    print(c,"is greater")
    
