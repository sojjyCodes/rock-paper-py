from random import randint
game = ["Rock", "Paper", "Scissors"]

computer = game[randint(0, 2)]
playersPoint = 0
computersPoint = 0

goOn = True
while goOn:
    player = input("Rock, Paper, Scissors? or  enter Finish to end!\n")
    if player == 'Finish':
        goOn = False
    elif(player == computer):
        print("Tie")
    elif(player == "Rock"):
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computersPoint = computersPoint + 1
        else:
                print("You win!", player, "smashes", computer)
                playersPoint = playersPoint + 1
    elif(player == "Paper") :
        if(computer == "Scissors"):
            print("You loose!", computer, "cuts", player)
            computersPoint = computersPoint + 1
        else:
            print("You win!", player, "covers", computer)
            playersPoint = playersPoint + 1
    elif(player == "Scissors"):
        if(computer == "Rock"):
            print("You loose!", computer, "smashes", player)
            computersPoint = computersPoint + 1
        else:
            print("You win", player, "cuts", computer)
            computersPoint = computersPoint + 1
    else:
        print("That is not a valid play. Check your spelling!")
        computer = game[randint(0,2)]
        print('********Next Turn**********')
        print("Player: ", playersPoint)
        print("Computer: ", computersPoint)
