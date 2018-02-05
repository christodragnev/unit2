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

if date.today().month == month and date.today().day == day:
    print('You turn ', 2018-year, ' years old today. Happy birthday!!')
elif month>date.today().month:
    print('You are ', 2017-year, 'years old')
else:
    print('You are ', 2018-year, 'years old')