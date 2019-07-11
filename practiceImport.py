import math
import calendar

def mathFunc():  #experimenting with imported Smath functions
    print(math.sqrt(4))  #2.0
    print(math.floor(10.2))  #10 because rounds decimal down.
    print(math.pi)
    print(math.e)

def calendarFunc():
    year=int(input("year #"))
    month = int(input("month #"))
    print(calendar.month(year,month))  #prints out columns and rows of the days of the month

mathFunc()
calendarFunc()
