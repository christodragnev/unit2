#Christo Dragnev
#1/31/18
#warmup3.py

num = int(input('Enter a integer: '))

if num%2==0 and num%3==0:
    print(num, 'is divisble by 2 and by 3')
elif num%2==0:
    print(num, 'is divisible by 2 and not 3')
elif num%3==0:
    print(num, 'is divisble by 3 and not 2')
else:
    print(num, 'is not divisble by 2 or 3')