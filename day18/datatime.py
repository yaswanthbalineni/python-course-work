'''
data time




import datetime


getting current date

from datetime import date
today=date.today()
print(today)

creating specific date

from datetime import date
specific=date(2023,4,1)
print(specific)


extracting year,month,day


from datetime import date
today=date.today()
print("year",today.year)
print("month",today.month)
print("day", today.day)



finding the day of the week



from datetime import date
today=date.today()
print("weekday(0=monday,6=sunday):",today.weekday())



from datetime import date
today=date.today()
print(" ISO weekday(1=monday,7=sunday):",today.isoweekday())



working with the time


from datetime import time
specific=time(20,30,5)
print(specific)


extracting hours minutes and seconds


from datetime import time
specific=time(20,30,5)
print(specific.hour)
print(specific.minute)
print(specific.second)



working with both datetime


from datetime import datetime
now= datetime.now()
print(now)





formatting dates and times

strftime()

import datetime
now = datetime.datetime.now()
fromatted_date=now.strftime("%y-%m-%d")
fromatted_time=now.strftime("%H:%M:%S")
fromatted_datetime=now.strftime("%d-%b-%y %I:%M %p")
print(fromatted_datetime,fromatted_time,fromatted_date)


strptime


import datetime
date_string="16-04-2023 14:30"
parsed_date = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M")
print(parsed_date)

timedelta
'''
from datetime import timedelta,datetime
today=datetime.today()
now=datetime.now()
next=today+timedelta(days=7)
print(next)
past=today-timedelta(days=6)
print(past)
future=now+timedelta(hours=4)
print(future)
