class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometre_reading = 0

	def get_descripitive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometre(self):
		print("This car has " + str(self.odometre_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descripitive_name())

my_new_car.odometre_reading = 23
my_new_car.read_odometre()