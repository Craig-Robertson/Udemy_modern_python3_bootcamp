##Rock Paper Scissors BASIC##
print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("enter Player 1's choice: ")
p2 = input("enter Player 2's choice: ")

print("SHOOT!")

if p1 == p2:
    print("it is a tie")
elif p1 == 'rock':
    if p2 == 'paper':
        print("player2 wins")
    elif p2 == 'scissors':
        print("player1 wins")
elif p1 == 'paper':
    if p2 == 'rock':
        print("player1 wins")
    elif p2 == 'scissors':
        print("player2 wins")
elif p1 == 'scissors':
    if p2 == 'rock':
        print("player2 wins")
    elif p2 == 'paper':
        print("player1 wins")
else:
    print("something went wrong...")