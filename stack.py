stack=[]
top=-1
m=int(input("Enter the range of stack: "))
counter = 0
while counter <= 10:
    num=int(input("Press----->1 to push \n press---->2 to pop\npress---->3 to display \n press---->4 to exit\n"))
    if (num is 1):
        data=int(input("Enter data : "))
        if top is m-1:
            print("Overflow")
            continue
        else:
            top=top+1
            stack.append(data)
            print(top)
    elif num is 2:
        if top is -1:
            print("Underflow")
        else:
            stack.pop(top)
            top=top-1
    elif num is 3:
        print(stack)
    elif num is 4:
        break
    else:
        print("You entered a wrong option")

