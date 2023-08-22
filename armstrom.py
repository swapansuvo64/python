for i in range(1,1001):
    sum=0
    temp=i
    while(temp>0):
        dig=temp%10
        sum+=dig**3
        temp//=10
    if sum == i:
        print(i)


    
