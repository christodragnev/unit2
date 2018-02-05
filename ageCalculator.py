#Christo Dragnev
#2/5/18
#ageCalculator.py

from datetime import date

date.today().day
date.today().month
date.today().year

year = int(input('Enter the year you were born: '))
month = int(input('Enter the month you were born: '))       #use number not name
day = int(input('Enter the day you were born: '))

if date.today().day==year and date.today().month == month and date.today().day == day
    print('Happy birthday!!')
else:
    print('You are ', 2018-year, 'years old')