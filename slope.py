#Christo
#2/2/18
#slope.py

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

if x2 - x1 == 0:
    print('The slope is undefined')
    print('The equation of the line is x=', x1)
else: 
    print('The slope is ', (y2 - y1)/(x2 - x1))
