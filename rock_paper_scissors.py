
# da sloja broqch na pobedite i stop
import random


player_win = 0
computer_win = 0

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors or: ")


    if player_move == "p":
        player_move = paper
    elif player_move == "r":
        player_move = rock
    elif player_move == "s":
        player_move = scissors
    else:
        print(f"You won {player_win}  Computer won {computer_win}")
        raise SystemExit("Invalid Input. Try again...")


    print(f"You pick {player_move}.")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
        print("You win!")
        player_win +=1
    elif player_move == computer_move:
        print("Draw!")
    else:
        print("You lose!")
        computer_win +=1