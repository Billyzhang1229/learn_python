destination = {}

active = True

while active:
	name = input("\nwhat is your name? ")
	response = input("If you could visit one place in the world, where would you go? ")

	destination[name] = response

	repeat = input("Would you like to let another person respound?(yes/ no) ")
	if repeat == 'no':
		active = False

print("\n--- Destination Result ---")
for name, response in destination.items():
	print(name.title() + " would like to go to " + response.title() + ".")