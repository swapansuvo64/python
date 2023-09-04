num=1

for i in range(0,2):
    for j in range(0,5):
        if j <i :
            print(" ",end=" ")
        else:
            print(num,end=" ")
            num=num+1
    print("\n")
    
