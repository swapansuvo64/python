import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
s=((a+b+c)/2)
area =(s*(s-a)*(s-b)*(s-c))
d= math.sqrt(area)
print("Area is: ",d)
