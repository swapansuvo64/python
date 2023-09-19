import calendar
y=int(input("Enter the year: "))
st=int(input("Enter the start year: "))
end=int(input("Enter the  end year: "))
if (calendar.isleap(y)):
    print("leap year")
else: print("Not leap")
print("%d and %d is" %(st,end),end="")
print(calendar.leapdays(st,end))
