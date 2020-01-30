import random

random_number = random.randint(1,10) #numbers 1-10

while True:
	guess = input("Guess a number: 1 to 10: ")
	guess = int(guess)
	if guess < random_number:
		print("higher")
	elif guess > random_number:
		print("lower")
	else:
		print("you won!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
		else:
			break
