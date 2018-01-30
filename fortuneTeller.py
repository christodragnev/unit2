#Christo Dragnev
#1/29/18
#fortuneTeller.py

color = str(input('Pick red or blue: '))
num = int(input('Pick a number from 1-4: '))

if color == 'red' and num == 1:
    print('You will be attacked by a bear')
elif color == 'red' and num == 2:
    print('You will be attacked by a shark')
elif color == 'red' and num == 3:
    print('You will be attacked by a dog')
elif color == 'red' and num == 4:
    print('You will be attacked by a god')
elif color == 'blue' and num == 1:
    print('You will be attacked by a whale')
elif color == 'blue' and num == 2:
    print('You will be attacked by a bird')
elif color == 'blue' and num == 3:
    print('You will be attacked by a lion')
elif color == 'blue' and num == 4:
    print('You will be a millionaire')
else:
    print('Bad input')