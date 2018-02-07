class User:

	def __init__(self, first_name, last_name, age, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = str(age)
		self.gender = gender

	def describe_user(self):
		print("These are the info:")
		print(
			self.first_name + ", " +
			self.last_name + ", " + 
			self.age + ", " +
			self.gender)

	def greet_user(self):
		print("Hello "+ self.first_name.title() + " " + self.last_name.title())

user_info = User('billy', 'zhang', 16, 'male')
user_info.describe_user()
user_info.greet_user()