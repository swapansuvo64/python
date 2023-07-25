import math
n=int(input("enter n"))
r=int(input("enter r"))
c=((math.factorial(n))/((math.factorial(r))*(math.factorial(n-r))))
p=((math.factorial(n))/(math.factorial(n-r)))
print(c,p)
