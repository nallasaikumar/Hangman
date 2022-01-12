from random_word import RandomWords

word = RandomWords().get_random_word().lower()
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print(len(word)*'_ ')
guess_list = []

wrong = 0

while wrong <= 6:
    
    start = 0
    last = len(letters)
    count = 0
    print(' '*27, end = ' ')
    while start < last:
        print(letters[start], end = ' ')
        count = count + 1
        if count == 7:
            print(end = '\n')
            print(' '*27, end = ' ')
            count = 0
        start = start + 1
        
    guess = input('\nEnter ur guess: ')
    letters.remove(guess.upper())
    guess_list.append(guess)
    
    if guess not in word:  # only wrong guess
        wrong = wrong + 1
        
    result = ''
    print()
    for letter in word:
        if letter in guess_list:
            result = result + letter
            print(letter, end = ' ')
        else:
            result = result + '_'
            print('_', end = ' ')
    print('')
    print('\n Result : ', result)
    print(' '*50, ' TURNS LEFT : ', 6 - wrong)
    if '_' not in result:
        print('USER WON - Congrats!')
        break
else:
    print('USER LOST', word)
