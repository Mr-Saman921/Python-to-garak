import calendar
import time

def print_calendar():
    c = calendar.TextCalendar(0)
    m = int(time.strftime("%m"))
    y = int(time.strftime("%Y"))
    for i in range(1, 13):
        return c.formatmonth(y, i)
    return c.formatmonth(y, m)

print(print_calendar())