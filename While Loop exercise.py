from random import randint

number = randint(1,10) # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number != 5:
	i += 1
    number = randint(1,10)
print(i)