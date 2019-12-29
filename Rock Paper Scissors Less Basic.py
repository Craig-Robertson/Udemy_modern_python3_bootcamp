##Rock Paper Scissors BASIC##
import random

print("...rock...")
print("...paper...")
print("...scissors...")

r = 'rock'
p = 'paper'
s = 'scissors'
rps = [r,p,s]

player = input("Player, make your move: ").lower()
computer = random.choice(rps).lower()
print("The computer plays: ",computer)

print("SHOOT!")

if player == computer:
    print("it is a tie")
elif player == r:
    if computer == p:
        print("The computer wins")
    elif computer == s:
        print("you win")
elif player == p:
    if computer == r:
        print("you win")
    elif computer == s:
        print("The computer wins")
elif player == s:
    if computer == r:
        print("The computer wins")
    elif computer == p:
        print("you win")
else:
    print("please enter a valid move")