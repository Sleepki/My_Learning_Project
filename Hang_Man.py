'''
How to play:
type 'play' to play the game
This game is very funny to play
if you want more words to play please add your words as you want
the game will random words to your guess
the original game will let you have 8 lifes to try your letter
if you enter the same letter game will not cut down your life (who will remember all trying moves right ?)
*** please enter letter in lower case ***

Type "play" to play the game, "exit" to quit:
>play

H A N G M A N\n

------

Input a letter:
>p

p-----
Input a letter:
>qwerty

You should input a single letter
p-----
Input a letter:
>w

No such letter in the word
Your life total are 7 left(s)
p-----
'''
import string
import random

word = ['python', 'java', 'kotlin', 'javascript']
while True:
    life_total = 8
    order = input('Type "play" to play the game, "exit" to quit:')
    if order == 'play':  # initialize game & random word to play
        random_word = random.choice(word)
        guess_word = '-' * len(random_word)
        list_letter = []
        win = False
        print('H A N G M A N\n')
        print(guess_word)
        while life_total != 0:  # Loop the game until win or lose
            input_letter = input('Input a letter:')
            if len(input_letter) != 1:  # input only 1 letter at a time
                print('You should input a single letter')
            elif input_letter not in string.ascii_lowercase:  # input should be in ASCII lowercase
                print('It is not an ASCII lowercase letter')
            elif input_letter in list_letter:  # check if letter is given twice
                print('You already typed this letter')
            else:
                for i in range(len(random_word)):  # if letter is correct show that letter in blind string
                    if input_letter == random_word[i]:
                        guess_word = guess_word[:i] + input_letter + guess_word[i + 1:]
                        list_letter.append(input_letter)
                if input_letter not in random_word:  # if letter is not correct your life total decrease by 1
                    print('No such letter in the word')
                    list_letter.append(input_letter)
                    life_total -= 1
                    print(f'Your life total are {life_total} left(s)')
            if life_total == 0:  # lose when life is 0
                print('You are hanged!')
                break
            if set(random_word).intersection(set(list_letter)) == set(random_word):  # win if correct all letter
                print('You guessed the word!\nYou survived!')
                break
            print(guess_word)
    elif order == 'exit':  # exit the game
        break
    else:  # Throw an unknown order type
        print(f'Sorry, option {order} is not recognized')
