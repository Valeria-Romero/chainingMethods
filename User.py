class User:
    allBankAccounts  = []
    def __init__(self, accountOwner, accountNumber):
        self.accountOwner = accountOwner
        self.accountNumber = accountNumber
        self.balance = 0.0
        User.allBankAccounts.append(self)

    def make_withdrawal (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            
        else:
            print("We cannot process your withdrawal")
            print(f"You current have {self.balance}.")
            print(f"And you are trying to withdraw {amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.accountOwner}, Balance: ${self.balance}.")
        return self

    def deposit (self, amount):
        self.balance += amount
        return self

    def transfer_money(self,amount,other_user):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self