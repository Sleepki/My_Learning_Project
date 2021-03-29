'''
How to use: (> sign is an input)
This is a credit card simulation
you will sign up for a credit card with real Validity check called Luhn Algorithm
when you sign up your data will be saved in local database


1. Create an account
2. Log into account
0. Exit
>1
Your card has been created
Your card number:
4000000200120014
Your card PIN:
9404

*** please remember your ID and PIN to continue your banking process

>2
Enter your card number:
>4000000200120014
Enter your PIN:
9404
You have successfully logged in!

Then you will be ask what action you want to do with your account
Balance - Check your balance
Add income - add your money to your account
Do transfer - transfer money to another account (need another account to transfer)
Close account - Delete your account
Log out - return to menu
Exit - shutdown system
'''


import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''create table if not exists card (id INTEGER PRIMARY KEY ,
                                number TEXT,
                                pin TEXT,
                                balance INTEGER default 0);''')
conn.commit()
System = True

'----------------------------------------------------------------------------'


def create_account():
    global account
    global pin
    account = '400000'
    for _ in range(9):
        account += str(random.randint(0, 9))
    pre_Luhn = [int(i) for i in account]
    for i in range(0, 15, 2):
        pre_Luhn[i] *= 2
    pre_Luhn = [i - 9 if i > 9 else i for i in pre_Luhn]
    sum_Luhn = sum(pre_Luhn)
    last_digit = abs(10 - (sum_Luhn % 10))
    if last_digit % 10 == 0:
        account += '0'
    else:
        account += str(last_digit)
    pin = ''
    for i in range(4):
        pin += str(random.randint(0, 9))
    print('Your card has been created')
    print('Your card number:')
    print(account)
    print('Your card PIN:')
    print(pin)
    print()
    cur.execute(f'INSERT INTO card (number, pin) VALUES ({account}, {pin})')
    conn.commit()


while System:
    First_page = input('1. Create an account\n2. Log into account\n0. Exit')
    if First_page == '1':
        create_account()
    elif First_page == '2':
        Enter_card = input('Enter your card number:')
        Enter_pin = input('Enter your PIN:')
        cur.execute(f'''SELECT * FROM card WHERE number = {Enter_card}
                    AND pin = {Enter_pin}''')
        pull = cur.fetchall()
        if pull is not None:
            print('You have successfully logged in!\n')
            while True:
                Order = input('''1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit''')
                if Order == '1':
                    query = f'SELECT balance FROM card WHERE number = {Enter_card} AND pin = {Enter_pin};'
                    cur.execute(query)
                    conn.commit()
                    pull = cur.fetchone()
                    print('Balance:', pull[0])
                    print()
                elif Order == '2':
                    cur.execute(f'SELECT balance FROM card WHERE number = {Enter_card};')
                    pull = cur.fetchone()
                    add = int(input('Enter income:'))
                    income = pull[0] + add
                    query = f'UPDATE card SET balance = {income} WHERE number = {Enter_card} AND pin = {Enter_pin};'
                    cur.execute(query)
                    conn.commit()
                    print('Income was added!\n')
                elif Order == '3':
                    cur.execute('SELECT * FROM card;')
                    conn.commit()
                    Check_ID = str(input('Transfer\nEnter card number:'))
                    pull_all = cur.fetchall()
                    list_Account = [pull_all[i][1] for i in range(len(pull_all))]
                    if Check_ID in list_Account:
                        if Check_ID == Enter_card:
                            print("You can't transfer money to the same account!")
                        else:
                            Tranfer = int(input('Enter how much money you want to transfer:'))
                            cur.execute(f'SELECT balance from card WHERE number = {Enter_card} AND pin = {Enter_pin};')
                            conn.commit()
                            Check_balance_with = cur.fetchone()
                            cur.execute(f'SELECT balance from card WHERE number = {Check_ID};')
                            conn.commit()
                            Check_balance_de = cur.fetchone()
                            if Tranfer <= Check_balance_with[0]:
                                Withdraw = Check_balance_with[0] - Tranfer
                                Deposit = Check_balance_de[0] + Tranfer
                                cur.execute(f'UPDATE card SET balance = {Withdraw} WHERE number = {Enter_card}')
                                conn.commit()
                                cur.execute(f'UPDATE card SET balance = {Deposit} WHERE number = {Check_ID}')
                                conn.commit()
                                print('Success!')
                            else:
                                print('Not enough money!')
                    else:
                        pre_Luhn = [int(i) for i in Check_ID[:15]]
                        for i in range(0, 15, 2):
                            pre_Luhn[i] *= 2
                        pre_Luhn = [i - 9 if i > 9 else i for i in pre_Luhn]
                        sum_Luhn = sum(pre_Luhn)
                        last_digit = abs(10 - (sum_Luhn % 10))
                        if last_digit % 10 == 0:
                            last_digit = 0
                        if str(last_digit) != Check_ID[-1]:
                            print('Probably you made a mistake in the card number. Please try again!')
                        else:
                            print('Such a card does not exist.')
                elif Order == '4':
                    cur.execute(f'DELETE FROM card WHERE number = {Enter_card};')
                    conn.commit()
                    print('The account has been closed!')
                    break
                elif Order == '5':
                    break
                elif Order == '0':
                    System = False
                    break
        else:
            print('Wrong card number or PIN!')
    elif First_page == '0':
        break
print('Bye!')
conn.close()