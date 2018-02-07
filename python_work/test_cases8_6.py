def city_country(city, country):

	places = {'city name': city, 'contry name': country}
	return places

while True:
	print("press 'quit' to end.")
	
	ci = input('city name: ')
	if ci == 'quit':
		break
	
	co = input('contry name: ')
	if co == 'quit':
		break

	city_country = city_country(ci, co)
	print(city_country) 