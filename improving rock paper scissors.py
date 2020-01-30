import random


r = 'rock'
p = 'paper'
s = 'scissors'
rps = [r,p,s]

player_wins = 0
computer_wins = 0 
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score: {player_wins}  Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    computer = random.choice(rps).lower()
    print("The computer plays: ",computer)

    if player == computer:
        print("it is a tie")
    elif player == r:
        if computer == p:
            print("The computer wins")
            computer_wins += 1
        elif computer == s:
            print("you win")
            player_wins += 1
    elif player == p:
        if computer == r:
            print("you win")
            player_wins += 1
        elif computer == s:
            print("The computer wins")
            computer_wins += 1
    elif player == s:
        if computer == r:
            print("The computer wins")
            computer_wins += 1
        elif computer == p:
            print("you win")
            player_wins += 1
    else:
        print("please enter a valid move")
if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("It is a tie")
else:
    print("Sorry, looks like the computer won this time")
