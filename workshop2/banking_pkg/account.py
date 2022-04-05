#show balance
def show_balance(balance):
    print("Current Balance $ " , float(balance))

# deposit
def deposit(balance):
    amount = input("Enter amount to Deposit:  ")
    return float(balance) + float(amount)

# withdraw
def withdraw(balance):
    amount = input("Enter amount to Withdraw ")
    return float(balance) - float(amount)
        

# logout
def logout(name):
    print("Goodbye " +  name + "!")