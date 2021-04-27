import datetime


def right_date (d,m,y):
    try:
        date = datetime.date(y, m, d)
        print(True)
    except:
        print(False)


d = int(input('Enter the day: '))
m = int(input('Enter the month: '))
y = int(input('Enter the year: '))
right_date(d, m, y)
