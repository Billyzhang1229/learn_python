class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		print("---------------------------------------------")
		print("The restaurant name is " + self.restaurant.title())
		print("Our cuisine type is " + self.cuisine)

	def open_resturant(self):
		print("\n" + self.restaurant.title() + " is opening.")
		print("---------------------------------------------")
the_resraurant = Restaurant('nandos', 'Portuguese')

the_resraurant.describe_restaurant()
the_resraurant.open_resturant()