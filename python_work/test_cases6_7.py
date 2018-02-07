people = {
    'billy_zhang': {
        'first_name': 'billy', 
        'last_name': 'zhang', 
        'age': 16, 
        'city': 'shijiazhuang',
    },
    'richard_li': {
        'first_name': 'richard',
        'last_name': 'li',
        'age': 16,
        'city': 'Seattle',
    },
    'tammy yeung': {
        'first_name': 'tammy',
        'last_name': 'yeung',
        'age': 16,
        'city': 'london',
    },
}

for people_name, people_info in people.items():
    print("\nPeople name: " + people_name)
    full_name = people_info['first_name'] + people_info['last_name']
    city = people_info['city']

    print("\tName: " + full_name.title())
    print("\tCity: " + city.title())