import calendar
from datetime import date
from datetime import timedelta
date  = date.today()
man=[]
date_2= date.replace(day=calendar.monthrange(date.year, date.month)[1])
while date<=date_2:
    print(date)
    date = date + timedelta(1)
    man.append(date)
