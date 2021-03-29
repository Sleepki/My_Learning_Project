"""
How to play: (Please Noted after '>' sign is an input)
Like an old school Tic-Tac-Toe game
X player will go first and how to place your token is enter a coordinate x and y between 1 to 3
Then O player will place token
There will be one player to win a game or game will be draw

example:
>1 3
---------
| X _ _ |
| _ _ _ |
| _ _ _ |
---------

>1 1
---------
| X _ _ |
| _ _ _ |
| O _ _ |
---------

>1 4
Coordinates should be from 1 to 3!
"""


def result():
    print(f'''---------
| {move[0]} {move[1]} {move[2]} |
| {move[3]} {move[4]} {move[5]} |
| {move[6]} {move[7]} {move[8]} |
---------''')


def place_X():
    global move
    while True:
        place = input('Enter the coordinates:').split()
        if place == ['1', '1']:
            if move[6] == '_':
                move = move[:6] + 'X' + move[7:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['1', '2']:
            if move[3] == '_':
                move = move[:3] + 'X' + move[4:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['1', '3']:
            if move[0] == '_':
                move = 'X' + move[1:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '1']:
            if move[7] == '_':
                move = move[:7] + 'X' + move[8:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '2']:
            if move[4] == '_':
                move = move[:4] + 'X' + move[5:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '3']:
            if move[1] == '_':
                move = move[:1] + 'X' + move[2:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '1']:
            if move[8] == '_':
                move = move[:8] + 'X'
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '2']:
            if move[5] == '_':
                move = move[:5] + 'X' + move[6:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '3']:
            if move[2] == '_':
                move = move[:2] + 'X' + move[3:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place[0].isdigit():
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


def place_O():
    global move
    while True:
        place = input('Enter the coordinates:').split()
        if place == ['1', '1']:
            if move[6] == '_':
                move = move[:6] + 'O' + move[7:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['1', '2']:
            if move[3] == '_':
                move = move[:3] + 'O' + move[4:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['1', '3']:
            if move[0] == '_':
                move = 'O' + move[1:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '1']:
            if move[7] == '_':
                move = move[:7] + 'O' + move[8:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '2']:
            if move[4] == '_':
                move = move[:4] + 'O' + move[5:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['2', '3']:
            if move[1] == '_':
                move = move[:1] + 'O' + move[2:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '1']:
            if move[8] == '_':
                move = move[:8] + 'O'
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '2']:
            if move[5] == '_':
                move = move[:5] + 'O' + move[6:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place == ['3', '3']:
            if move[2] == '_':
                move = move[:2] + 'O' + move[3:]
                break
            else:
                print('This cell is occupied! Choose another one!')
        elif place[0].isdigit():
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


def check_win():
    global X, O
    i = 0
    X = 0
    O = 0
    # Check row
    for _ in range(3):
        if move[i] == 'X' and move[i + 1] == 'X' and move[i + 2] == 'X':
            print('X wins')
            X += 1
            break
        if move[i] == 'O' and move[i + 1] == 'O' and move[i + 2] == 'O':
            print('O wins')
            O += 1
            break
        i += 3
    # check column
    for i in range(3):
        if move[i] == 'X' and move[3 + i] == 'X' and move[6 + i] == 'X':
            print('X wins')
            X += 1
            break
        if move[i] == 'O' and move[3 + i] == 'O' and move[6 + i] == 'O':
            print('O wins')
            O += 1
            break
    # Check diagonal
    if move[0] == 'X' and move[4] == 'X' and move[8] == 'X':
        X += 1
        print('X wins')
    elif move[2] == 'X' and move[4] == 'X' and move[6] == 'X':
        X += 1
        print('X wins')
    elif move[0] == 'O' and move[4] == 'O' and move[8] == 'O':
        O += 1
        print('O wins')
    elif move[2] == 'O' and move[4] == 'O' and move[6] == 'O':
        O += 1
        print('O wins')


def Check_Draw():
    global Checked
    Checked = 0
    if move.count('X') + move.count('O') == 9:
        Checked += 1
        print('Draw')


def main():
    result()
    while True:
        place_X()
        result()
        check_win()
        if O > 0 or X > 0:
            break
        Check_Draw()
        if Checked == 1:
            break
        check_win()
        place_O()
        result()
        check_win()
        if O > 0 or X > 0:
            break
        Check_Draw()
        if Checked == 1:
            break


allmove = [['1', '1'], ['1', '2'], ['1', '3'], ['2', '1'], ['2', '2'], ['2', '3'], ['3', '1'], ['3', '2'], ['3', '3']]
move = '_________'
main()
