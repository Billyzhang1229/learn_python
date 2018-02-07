def build_profile(first, last, **user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key, value in user_info.items(): 
		profile[key] = value
	return profile

user_profile = build_profile('billy', 'zhang',
							location = 'london',
							filed = 'computer science',
							gender = 'male',)
print(user_profile)