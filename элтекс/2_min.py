import sched, time

m = sched.scheduler(time.time, time.sleep)

def f():
    m.enter(108, 2, f )  # Перезапуск через 2 min
    print(time.time())

f()
m.run()
