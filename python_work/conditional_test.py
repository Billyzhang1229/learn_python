#1
car = 'audi'
bus = 'audi'
print(car == bus)

#2
car = "Audi"
bus = "AUDI"
print(car.lower() == bus.lower())

#3
print(23 == 24)
print(23 != 24)
print(23 > 24)
print(23 < 24)
print(23 >= 24)
print(23 <= 24)

#4
number_1 = 23
number_2 = 25
print(number_1 < 24 and number_2 > 24)
print(number_1 > 24 or number_2 >24)

#5
cars = ['audi', 'bmw', 'subaru', 'benz']
car = 'audi'

if car in cars:
	print(car.title() + ' is in the list.')

#6
cars = ['audi', 'bmw', 'subaru', 'benz']
car = 'suzuki'

if car not in cars:
	print(car.title() + ' is not in the list.')