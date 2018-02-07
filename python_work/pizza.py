pizza = {
    'crust': 'thick',
    'toppings': ['mushmrooms', 'extra cheese'],
    }

print("You ordered a " + pizza['crust'] + "-crust pizza" +
	' with the following toppings:')

for topping in pizza['toppings']:
	print(topping)