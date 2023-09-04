bigp=input("Enter your pharse : ")
subp=input("Enter your sub-pharse : ")

print(subp in bigp)

subp_list=list(subp)
length2=len(subp)


bigp_list=list(bigp)
length1=len(bigp)



for i in range(0,length1-1):
    for j in range(0,length2-1):
        if bigp_list[i] is subp_list[j]:
           start= i
           end=i+(length2-1)
           break
        break  
print(start,end)

