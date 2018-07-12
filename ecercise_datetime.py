
from datetime import date
from datetime import timedelta


a = date.today()
next_day =  date.today() + timedelta(days=1)

print(next_day)

