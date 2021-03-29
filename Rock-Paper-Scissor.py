'''
How to play : (Please Noted after '>' sign is an input)
*** You need to create plain rating.txt at the same directory of this file for collect score ***
when start please enter your name then you will be select mode to play with computer

please select mode to play
> (Enter)
Okay, let's start
Type your move

> paper
There is a draw (paper)

>paper
Well done. The computer chose rock and failed

>!rating
100

>!exit
Bye!

*** if you want more option in game ***

please select mode to play

>water,dragon,devil,paper,rock,snake,air,lightning etc.
Okay, let's start
Type your move

'''

import random


rule = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

file = open('rating.txt', 'r')
name = input('Enter your name:')
score = 0
for i in file:
    if i.split()[0] == name:
        score = int(i.split()[1])
print(f'Hello, {name}')
file.close()
mode = input('please select mode to play '
             '(Press Enter for normal mode if you want more choice please enter each option you want on rule )')
if mode == '':
    option = ['paper', 'scissors', 'rock']
else:
    option = mode.split(',')
print("Okay, let's start")
print("!rating for score and !exit for exit the game (your score will be saved)")
while True:
    computer_pick = random.choice(option)
    player_pick = input('Type your move')
    if player_pick in option:
        if player_pick == computer_pick:
            print(f'There is a draw ({player_pick})')
            score += 50
        elif computer_pick not in rule[player_pick]:
            print(f'Sorry, but the computer chose {computer_pick}')
        elif computer_pick in rule[player_pick]:
            print(f'Well done. The computer chose {computer_pick} and failed')
            score += 100
    elif player_pick == '!exit':
        print('bye!')
        break
    elif player_pick == '!rating':
        print(f'{score}')
    else:
        print('Invalid input')
