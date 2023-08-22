try:
    hours=int(input("enter hours: "))
    rate=int(input("enter rate: "))
except:
    hours='n'
    rate='n'
if hours is 'n' and hours is 'n' :
    raise Exception("You enter Charecter not an integer")
elif hours < 40 :
    pay = hours*rate
    print("The payment is",pay)
elif hours>= 40 :
     pay = ((hours-40)*rate)*1.5+ (hours*rate)
     print("The payment is",pay)
else:
    print("Your enter wrong")

    
