class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        new_balance = self.cents + deposit_cents + self.dollars * 100 + deposit_dollars * 100
        self.dollars = new_balance // 100
        self.cents = new_balance % 100


# myObj = PiggyBank(1, 1)
# print(myObj.dollars, myObj.cents)
#
# myObj.add_money(500, 500)
# print(myObj.dollars, myObj.cents)
