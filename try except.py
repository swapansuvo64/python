 try:
    x=int(input("enter a number"))
except:
    x='n'
if x is 'n':
    pass
elif x%2==0:
    print("even")
else:
    print("odd")
