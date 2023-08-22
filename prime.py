num=int(input("Enter your number"))
f=0
for i in range (1,int(num+1)):
        if num % i is 0:
            f=f+1
if(f==2):
    print("prime")
elif(f==0):
    print("not prime")
