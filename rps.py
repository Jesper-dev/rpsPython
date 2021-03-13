from random import randint

#A list of play options
t = ["Rock", "Paper", "Scissors"]

#A random play to the computer
computer =t[randint(0,2)]

#Set player to false
player = False

while player == False:
    #Set player to True
    player = input("Rock, Paper, Scissors?")
    #Conditions
    if player == computer:
        print("tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    #If the player types something thats not Rock, Paper och Scissors
    else:
        print("That's not a valid play. Check your spelling!")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

