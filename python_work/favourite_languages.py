favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
    }
print("sarah's favourite_language is " +
	favourite_languages['sarah'].title() +
	".")

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is "+
		language.title() + ".")