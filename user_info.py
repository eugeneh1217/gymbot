import datetime

gymtime = input("what gym time do you want? dd/mm/yyyy/hh")
day = int(gymtime[-13:-11])
month = int(gymtime[-10:-8])
year = int(gymtime[-7:-3])
hour = int(gymtime[-2:])

weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

x = datetime.datetime(year, month, day, hour)

gymday = x.weekday()
gymdaystr = weekdays[gymday]

#Weekday, Month day, year (THURSDAY, DECEMBER 3, 2020)
gymmonth = x.strftime("%B") 
gym_date_final = (str(gymdaystr) + ", " + str(gymmonth) + " " + str(day) + ", " + str(year))
print(gym_date_final.upper())

#9:00 AM TO 9:45 AM
if hour >= 9:
    gym_time_final = (str(hour) + ":00 AM TO " + str(hour) + ":45 AM")
else:
    gym_time_final = (str(hour) + ":00 PM TO " + str(hour) + ":45 PM")
print(gym_time_final)



