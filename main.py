from User import User

markAccount = User("Mark Simmons", 100)
lilyAccount = User("Lily Addams", 250)
oscarAccount = User("Oscar Martinez", 123)


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
markAccount.deposit(156).deposit(223).deposit(150).make_withdrawal(285).display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
lilyAccount.deposit(1600).deposit(235).make_withdrawal(150).make_withdrawal(80).display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
oscarAccount.deposit(2500).make_withdrawal(135).make_withdrawal(58).make_withdrawal(650).display_user_balance()

#Have the first user transfer money to the third user and then print both users' balances
markAccount.transfer_money(10,oscarAccount)