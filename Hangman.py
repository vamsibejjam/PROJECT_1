import time, random

print(' Are u ready to play HANGMAN!..... ')
time.sleep(2)  # Execution start after 2 secs....
print(' OK..let\'s play HANGMAN!..... ')

with open('words.txt') as file:  # Opening a words.txt file placed in same directory........
    x = file.read()
    words_list = x.split(' ')  # List  of words in words.txt file stored in variable


# Repeat Function to ask game again.........................................
def repeat():
    choice = input('\n' + ' ' * 10 + 'Want to play again...type \'y/n\':').lower()
    if choice == 'y':
        hangman()
    else:
        print('\n' + ':)  Thanks for playing...hope you enjoyed..bye')


# Repeat function ends.......................................................

# Hangman Function to guess letters in a word..................................
def hangman():
    guess_word = random.choice(words_list)  # Random word selected from list
    time.sleep(1)
    print('\n' + ' Guess the', len(guess_word), 'length word...Buddy!')
    time.sleep(0.5)
    z = 0
    guessed_word = ''

    # for loop starts here........................................................................................
    for i in range(len(guess_word)):
        chances = 4
        guessed_letter = input(
            ' ' * 10 + 'Guess  letter %d  of word:' % (i + 1)).lower()  # give only lower case letters
        # --------------------------------------------------------------------------------------------------
        if guessed_letter == guess_word[i].lower():
            print(' ' * 10 + 'Your Guessed  letter  is right.......' + '\n')
        else:
            print(' ' * 10 + 'Your guess is wrong......')
            while chances != 0:
                print('\n' + ' ' * 10 + 'you have only %d chances left' % chances, 'to guess  letter %d' % (i + 1))
                if chances == 1:
                    print(
                        '\n' + 'This is your last chance buddy,if u guess u will go to next letter otherwise you lose')
                guessed_letter = input(
                    ' ' * 10 + 'Guess  letter %d  of word:' % (i + 1)).lower()  # give only lower case letters
                if guessed_letter == guess_word[i].lower():
                    print(' ' * 10 + 'Your Guessed  letter  is right.......' + '\n')
                    break
                chances -= 1
        # --------------------------------------------------------------------------------------------------
        if chances == 0:
            z += 1
            print('\n' + '    Oh! you lost..' + '''
                     +---+
                     |   |
                     O   |
                    /|\  |
                    / \  |
                         |
                ===========''')
            repeat()
            return
        # End for loop.................................................................................................

    if z == 0:
        print('\n' + ' :)  Hey! you won the game......')
        repeat()


# Hangman function ends................................................................................................


if __name__ == '__main__':
    hangman()
