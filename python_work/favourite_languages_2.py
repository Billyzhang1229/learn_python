favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print('\n' + name.title())

    if name in friends:
        print("Hi " + name.title() + 
            ", I see your favourite language is " + 
            favourite_languages[name].title())

if 'erin' not in favourite_languages:/\
	print('\nErin, please take you poll')