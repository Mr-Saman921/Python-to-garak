import calendar

def save_calendar_html(year, filename):
    html_calendar = calendar.HTMLCalendar(calendar.SUNDAY)
    calendar_html = html_calendar.formatyear(year)

    with open(filename, 'w') as file:
        file.write(calendar_html)

save_calendar_html(2024, 'calendar.html')
