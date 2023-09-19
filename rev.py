def  rev(x):
    temp=x
    y=x[::-1]
    print(y)
    if x is y:
        print("Palindrom")
x=input("enter: ")
rev(x)
