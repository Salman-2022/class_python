#using datetime module to print todays date


import datetime as dt
current_date = dt.date.today()

print(current_date)






#to print year,month and day separately

import datetime as dt
current_date = dt.date.today()

print('year',current_date.year)
print('month',current_date.month)
print('day',current_date.day)







#importing datetime all at once


import datetime as dt

current_datetime = dt.datetime.now()

print(current_datetime)
