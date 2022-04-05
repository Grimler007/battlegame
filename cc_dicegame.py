import random
high_score = 0
def dice_game():
    while True:
        global high_score
        print("Current High Score: ",  high_score)
        print(" 1) Roll Dice")
        print(" 2) Leave Game")
        player_choice = input("Enter your choice:")

        if player_choice == "1":
            roll1 = random.randint (1, 6)
            roll2 = random.randint (1, 6)
            my_score = roll1 + roll2 
            print("You roll a... ", roll1 )
            print("You roll a... ", roll2 )
            print("You have rolled a total of: ", my_score )

            if my_score > high_score:
                print("Congratulations you have a new High score!")                 
        elif player_choice =="2":
            print("goodbye?")
            break
        else:
            print("Not a valid option!")


dice_game()
