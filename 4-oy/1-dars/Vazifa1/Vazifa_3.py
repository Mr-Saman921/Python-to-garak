from datetime import date

def check_date(date1, date2):
    if date1 > date2:
        return date1 - date2

    else:
        return date2 - date1

date1 = date(2024, 7, 18)
date2 = date(2024, 8, 18)
print(check_date(date1, date2))
