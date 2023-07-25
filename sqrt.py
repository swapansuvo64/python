
import cmath
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
root= cmath.sqrt((b*b)-(4*a*c))
print(root)
x=((-b+root)/2*a)
y=((-b-root)/2*a)
print(x,y)
      
