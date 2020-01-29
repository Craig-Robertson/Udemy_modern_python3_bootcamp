##My solution##

# print("Hey how's it going?")
# data = input()
# while data != "stop copying me":
# 	print(data)
# 	data = input()
# print("UGH FINE YOU WIN")

## Slightly less verbose versions ##
print("Hey how's it going?")
data = input()
while data != "stop copying me":
	data = input(f"{data}\n")
print("UGH FINE YOU WIN")