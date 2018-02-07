def make_car(brand, model, **other_info):
	profile = {}
	profile["car's_brand"] = brand
	profile["model_name"] = model
	for key, value in other_info.items():
		profile[key] = value
	return profile

car = make_car('subaru', 'outback', colour='blue', tow_package=True)
print(car)