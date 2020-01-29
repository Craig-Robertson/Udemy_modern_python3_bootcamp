# while True:
# 	command = input("Type 'exit' to exit: ")
# 	if (command == "exit"):
# 		break


# for x in range(1, 101):
# 	print(x)
# 	if x == 3:
# 		break

times = input("How many times do I have to tell you this? ")
times = int(times)
for time in range(times):
	print(f"time {time+1}: Clean your room !")
	if time >= 4:
		print("Do you even listen anymore?")
		break
