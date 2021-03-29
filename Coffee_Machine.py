'''
This is a simulation of coffee machine
when run machine will ask you for action
buy - you will be ask what you want to buy
    if you buy any product materials will be reduced
    if any materials low the machine will warn what is missing
fill - each raw materials will be ask to refill in
take - all the money in machine will be taken
remaining - monitoring all materials in machine
exit - shut system down

'''
import time


class CoffeeMachine:
    # start machine with amount of materials
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    # Show current materials
    def status(self):
        print(f'The coffee machine has: {self.water} of water\n'
              f'{self.milk} of milk\n'
              f'{self.coffee_beans} of coffee beans\n'
              f'{self.disposable_cups} of disposable cups\n'
              f'{self.money} of money')

    # Buy some product or back to menu
    def buy(self):
        menu_options = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
        buy = input(menu_options)
        if buy == '1':
            if self.water >= 250 and self.coffee_beans >= 16:
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee_beans < 16:
                print('Sorry, not enough coffee beans!')
        elif buy == '2':
            if self.water >= 350 and self.coffee_beans >= 20 and self.milk >= 75:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 350:
                print('Sorry, not enough water!')
            elif self.coffee_beans < 20:
                print('Sorry, not enough coffee beans!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
        elif buy == '3':
            if self.water >= 200 and self.coffee_beans >= 12 and self.milk >= 100:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.coffee_beans < 12:
                print('Sorry, not enough coffee beans!')
        elif buy == 'back':
            print('Backing to main menu')
            time.sleep(1.5)
            pass
        else:
            print(f'Sorry, {buy} option is not recognized')
            CoffeeMachine.buy(self)

    # filling materials
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.disposable_cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        print()
        CoffeeMachine.status(self)

    # take all the money from machine
    def take(self):
        print(f'I gave you $ {self.money}')
        self.money = 0

    # Machine System model
    def system(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.status()
            elif action == 'exit':
                break
            else:
                print(f'Sorry, {action} action is not recognized')


def main():
    starting_machine = CoffeeMachine(400, 540, 120, 9, 550)
    starting_machine.system()


if __name__ == '__main__':
    main()
