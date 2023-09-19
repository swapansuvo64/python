x=int(input("Enter the number: "))
def fac(x):
    for i in range (1,int(x+1)):
        if x%i == 0:
            print(i)

fac(x)
