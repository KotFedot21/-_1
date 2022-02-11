
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

name = ("Алексей","Игорь", "Александр", "Владислав")

y_pos = np.arange(len(name))
speed = [8, 7, 12, 4]
plt.bar(y_pos, speed, align='center', alpha=0.5)
plt.xticks(y_pos, name)
plt.ylabel('Задачи ')
plt.title('Сотрудники')

plt.show()



"""def information_for_the_day ():
    current_date = datetime.datetime.today().replace(microsecond=0)
    print(current_date)
    zero_time = current_date - timedelta(minutes=current_date.minute,seconds=current_date.second,hours=current_date.hour)##получаем начало дня
    print (zero_time)
    while zero_time <= current_date :
        print ("информация за 5 минуту ")
        zero_time= zero_time + timedelta(minutes=5)
        print(zero_time)
information_for_the_day()
"""
