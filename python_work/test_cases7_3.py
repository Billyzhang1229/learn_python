number = "Check if the number is an integral multiple of 10."
number += "\nEnter a number: "

num = input(number)
num = int(num)

if num % 10 == 0:
	print("It is an integral multiple of 10.")
else:
	print("It isn't an integral multiple of 10.")