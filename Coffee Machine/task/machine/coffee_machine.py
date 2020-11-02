class Machine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water_has = water
        self.milk_has = milk
        self.coffee_has = coffee
        self.cups_has = cups
        self.money_has = money
        self.menu()

    def menu(self):
        while True:
            option = input("Write action (buy, fill, take, remaining, exit):")
            if option == "buy":
                self.buy()
            if option == "fill":
                self.fill()
            if option == "take":
                self.take()
            if option == "remaining":
                self.remaining()
            if option == "exit":
                exit()

    def buy(self):
        # global water_has, milk_has, coffee_has, cups_has, money_has
        selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

        if selection == '1':
            if self.water_has >= 250 and self.coffee_has >= 16 and self.cups_has >= 1:
                print("I have enough resources, making you a coffee!")
                self.water_has -= 250
                self.coffee_has -= 16
                self.cups_has -= 1
                self.money_has += 4
            else:
                if self.water_has < 250:
                    print("Sorry, not enough water!")
                if self.coffee_has < 16:
                    print("Sorry, not enough coffee!")
                if self.cups_has < 1:
                    print("Sorry, not enough cups!")

        elif selection == '2':
            if self.water_has >= 350 and self.milk_has >= 75 and self.coffee_has >= 20 and self.cups_has >= 1:
                print("I have enough resources, making you a coffee!")
                self.water_has -= 350
                self.milk_has -= 75
                self.coffee_has -= 20
                self.cups_has -= 1
                self.money_has += 7
            else:
                if self.water_has < 350:
                    print("Sorry, not enough water!")
                if self.milk_has < 75:
                    print("Sorry, not enough milk!")
                if self.coffee_has < 20:
                    print("Sorry, not enough coffee!")
                if self.water_has < 1:
                    print("Sorry, not enough cups!")

        elif selection == '3':
            if self.water_has >= 200 and self.milk_has >= 100 and self.coffee_has >= 12 and self.cups_has >= 1:
                print("I have enough resources, making you a coffee!")
                self.water_has -= 200
                self.milk_has -= 100
                self.coffee_has -= 12
                self.cups_has -= 1
                self.money_has += 6
            else:
                if self.water_has < 200:
                    print("Sorry, not enough water!")
                if self.milk_has < 100:
                    print("Sorry, not enough milk!")
                if self.coffee_has < 12:
                    print("Sorry, not enough coffee!")
                if self.cups_has < 1:
                    print("Sorry, not enough cups!")
        elif selection == 'back':
            self.menu()
        else:
            print("Choice not available")

    def fill(self):
        self.water_has += int(input("Write how many ml of water do you want to add:"))
        self.milk_has += int(input("Write how many ml of milk do you want to add:"))
        self.coffee_has += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups_has += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        self.money_has
        print("I gave you $", self.money_has)
        self.money_has = 0

    def remaining(self):
        print("\nThe coffee machine has:")
        print(self.water_has, "of water")
        print(self.milk_has, "of milk")
        print(self.coffee_has, "of coffee beans")
        print(self.cups_has, "of disposable cups")
        print(self.money_has, "of money")


my_machine = Machine(400, 540, 120, 9, 550)
