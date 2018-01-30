#Christo Dragnev
#1/30/18
#adventure.py

print('A man holding a bat is running at you')
print('You sprint home')
scenario1 = input('Do you call the police? ')
if scenario1 == 'yes':
    print('The police come too late and you get whacked')
elif scenario1 == 'no':
    print('Luckily, you find a gun on the ground and grab it')
    print('However, the man has opened the door and is about to hit you')
    scenario2 = input('Do you shoot him? ')
    if scenario2 == 'yes':
        print('He dies and you live happily ever after')
    elif scenario2 == 'no':
        print('He hits you and you die')
