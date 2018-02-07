def describe_city(city = 'rekjavik', country = 'iceland'):
	"""describe a city in which country"""
	print(city.title() + " is in " + country.title())

describe_city()
describe_city(city = 'new york', country = 'america')
describe_city(city = 'paris', country = 'france')