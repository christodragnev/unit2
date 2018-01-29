#Christo Dragnev
#1/29/18
#movie.py

age = float(input('Enter your age: '))

if age >= 18:
    print('You can watch R movies')
elif age>=13:
    print('You can watch PG-13 movies')
else:
    print('You can watch PG movies')
