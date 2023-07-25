u=int(input("Enter initial velocity"))
v=int(input("Enter final velocity"))
t=int(input("Enter time"))
m=int(input("Enter mass"))
a=((v-u)/t)
f=m*a
print(f)
if (f<0) :
    print("declaration and backward")
else :
    print("accelaretion and forward")
