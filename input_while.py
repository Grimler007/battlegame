while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Break out of infinte loop")
    option = input("Pick an Option:")
    if option == "1":
        print("You choose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid Comand")
print ("You have left the loop")