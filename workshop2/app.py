from banking_pkg.account import show_balance, deposit, withdraw, logout
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("        ===== Automated Teller machine ======")

# limit name 
while True:
    name = input("Enter name to register: ")
    if 0< len(name) <11:
        break
    elif len(name) >= 11:
        print("The maxium name length is 10 characters")
    else:
        print("You must enter a name")


pin = input("Enter PIN:")
balance = 0
print(name + " has been registered with a starting balance of $" + str(balance))

# logging in 
while True:
    print("        ===== Automated Teller machine ======")
    print("LOGIN")
    name_to_valiadate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")


    if (name_to_valiadate == name and pin_to_validate == pin):
            print("login successful!")
            break
        
    else:
        print("Invalid credentials \n ") 
#a deposit , witdraw and log out 
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        show_balance(balance)

    elif option == "2":
      balance =  deposit(balance)
      show_balance
# bonus withdraw check thing 
    elif option == "3":
        balance = withdraw(balance)
        
        
    elif option == "4":
        logout(name)
        break