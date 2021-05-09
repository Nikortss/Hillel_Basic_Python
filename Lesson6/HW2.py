import time
from datetime import datetime

def countdown(func):
    def timer():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func()
    return timer


@countdown
def what_time_is_it_now():
    now_time = datetime.now()
    str_time = now_time.strftime("%H:%M")
    print(str_time)


what_time_is_it_now()
