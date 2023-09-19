import calendar
yy=int(input("Enter a year"))
for month in range (1,13):
    mycal=calendar.monthcalendar(yy,month)
    week1=mycal[0]
    w2=mycal[1]
    if week1[calendar.MONDAY]!=0:
        auditday=week1[calendar.MONDAY]
    else:
        auditday=w2[calendar.MONDAY]
        for i in range (auditday):
            temp=i
    print("%10s %2d %2d"%(calendar.month_name[month],auditday, temp))
