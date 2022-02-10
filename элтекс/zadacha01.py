
from datetime import date
import datetime
from datetime import timedelta
import calendar
## если хотим определить за последнюю неделю
##1
def information_for_the_week():
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
#information_for_the_week()

##1

##информация за 1 день
##2
def information_for_the_day ():
    current_date = datetime.datetime.today().replace(microsecond=0)
    print(current_date)
    zero_time = current_date - timedelta(minutes=current_date.minute,seconds=current_date.second,hours=current_date.hour)##получаем начало дня
    print (zero_time)
    while zero_time <= current_date :
        print ("информация за 5 минуту ")
        zero_time= zero_time + timedelta(minutes=5)
        print(zero_time)
#information_for_the_day()

##даты записанны в список для дальнейшего сравнения
##3
def development_list():
    current_date = datetime.datetime.today().replace(microsecond=0)
    print(current_date)
    zero_time = current_date - timedelta(minutes=current_date.minute,seconds=current_date.second,hours=current_date.hour)##получаем начало дня
    print (zero_time)
    while zero_time <= current_date :
        ##print ("информация за 5 минуту ")
        zero_time= zero_time + timedelta(minutes=5)
        time_interval=[]
        time_interval.append(zero_time)
        print(time_interval)

## принимает дату введенную с клавиатуры
"""
print("Введите дату начала ")
year_start = int(input("Введите год: "))
month_start = int(input("Введите месяц: "))
day_start = int(input("Введите день: "))
date_start = date(year_start, month_start, day_start)
print("Введите дату конца")
year_end = int(input("Введите год: " ))
month_end = int(input("Введите месяц: "))
day_end =int(input("Введите день: "))
date_end = date(year_end, month_end, day_end)
print(date_start)
print(date_end)

"""
