''' day_week_born.py
ask to enter a birthday and show the day of the week the person was born
some dates in history ...
July 4, 1776 was on a Thursday
December 7, 1941 was on a Sunday
3/14/1879 was on a Friday (Albert Einstein's birthday aka. pi-day)
tested with Python32/33  by  vegaseat  14feb2013
'''

import datetime as dt
def get_day(birthday_str):
    while True:
        # stay in the loop until correct date is entered
        try:

            mth, day, yr = birthday_str.split('/')
            birthday = dt.date(int(yr), int(mth), int(day))
            if int(yr) > 1700:
                break
        except:
            print("Please enter correct date!")
            birthday_str = input('Enter birthday (format mm/dd/yyyy):')


    week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    return week_day[dt.date.weekday(birthday)]

# sf = "If you were born on %s, you were born on a %s"
#print(sf % (birthday_str, week_day[dt.date.weekday(birthday)]))
