from math import pi 
volume = (4.0/3) * pi * pow(5, 3)
print(volume) # 523.598775598

price = 24.95 * 0.6 * 60 + 3 + 0.75 * 59
print(price) # 945.45

import datetime
start_time = datetime.datetime(2008, 8, 8, 6, 52)
time_spent_in_sec = (8 * 60 + 15) * 2 + (7 * 60 + 12) * 3
end_time = start_time + datetime.timedelta(seconds=time_spent_in_sec)
print(end_time) # 2008-08-08 07:30:06

