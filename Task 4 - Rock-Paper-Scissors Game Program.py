#Rock-Paper-Scissors Program

import random


choices = ("rock", "paper", "scissors")
player = None
opponent = random.choice(choices)
playing = True

while playing:
    player = None
    opponent = random.choice(choices)

    while player not in choices:
        player = input("Enter a choice (rock, paper, scissors): ")

        print("Player: ", player)
        print("Opponent: ",opponent)

        if player == opponent:
            print("Tie!")
        elif player == "rock" and opponent == "scissors":
            print("Rock beats Scissors")
            print("You Win!")
        elif player == "scissors" and opponent == "paper":
            print("Scissors beat Paper")
            print("You Win!")
        elif player == "paper" and opponent == "rock":
            print("Paper beats Rock")
            print("You Win!")
        else:
            print("Oh No...")
            print("You Lose!")

        play_again = input("Do You Want To Play Again?(yes/no): ").lower()
        if play_again == "yes":
            playing = True
        elif play_again == "no":
            playing = False
        else:
            print("Invalid option")
            exit()

print("Thank You For Playing!")
