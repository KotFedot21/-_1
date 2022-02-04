
from datetime import date
import datetime
from datetime import timedelta
import calendar
## если хотим определить за последнюю неделю
##1
"""
current_date = date.today()## дата сегодня
print(current_date)
print(current_date.weekday())##номер недели, 0-понедельник
num = current_date.weekday()

monday_date = current_date - timedelta(days=num)##получаем дату понедельника
print(monday_date)
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
##print (num)
i = 0
while i <= num :
    print ("информация за ", i,"день")
    monday_date = current_date + timedelta(1)
    i += 1
 """
##1

##информация за 1 день
##2
current_date = datetime.datetime.today().replace(microsecond=0)
print(current_date)
zero_time = current_date - timedelta(minutes=current_date.minute,seconds=current_date.second,hours=current_date.hour)##получаем начало дня
print (zero_time)
