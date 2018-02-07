numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
	if number is '1':
		print(number + "st")
	elif number is '2':
		print(number + 'nd')
	elif number is '3':
		print(number + 'rd')
	else:
		print(number +'th')