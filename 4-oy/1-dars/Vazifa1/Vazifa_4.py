import time

def time_printer():
    return time.strftime("Today:\n%A %d %B %Y %H:%M:%S\n%d.%m.%Y")

print(time_printer())
