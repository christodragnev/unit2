#Christo Dragnev
#2/12/18
#quiz2.py

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if len(word1)>len(word2):
    print('The first word is longer')
elif len(word2)>len(word1):
    print('The second word is longer')
else:
    print('Both words are equal in length')

if 'p' in word1 and 'p' in word2:
    print('Both words have a p')
elif 'p' in word2:
    print('The second word has a p')
elif 'p' in word1:
    print('The first word has a p')
else:
    print('Neither of the words has a p')
    
print('Enter two numbers that add up to 12: ')
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

if number1+number2 == 12:
    print('correct')
else:
    print('incorrect')
    
