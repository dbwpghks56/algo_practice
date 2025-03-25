import sys

sys.stdin = open('/Users/yujehwan/Desktop/algorithm/2025-03-25/input_1340.txt')
monthDays = sys.stdin.readline()
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
totalDay = 365

manmonth, mantime = monthDays.split(',')

month, day = manmonth.split()
year, time = mantime.split()
hour, minute = time.split(":")

hour = int(hour)
minute = int(minute)
year = int(year)
day = int(day)

if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
    days[1] = 29
    totalDay += 1

monthIndex = months.index(month)

elapsedDays = sum(days[:monthIndex]) + day
totalMinutes = totalDay * 24 * 60
elapsedMinutes = ((elapsedDays - 1) * 24 * 60) + (hour * 60) + minute
totalProgress = (elapsedMinutes / totalMinutes) * 100

# dayPer = (day / days[monthIndex -1]) * (100 / 12)
# monthPer = ((monthIndex - 1)  / 12) * 100
# hourPer = (hour / 24) * (100 / totalDay)
# minutePer = (minute / 60) * (100 / (totalDay * 24))

# print(monthPer)
# print(dayPer + monthPer + hourPer + minutePer)
print(totalProgress)
