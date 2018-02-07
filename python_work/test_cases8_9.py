def make_great(magicians_name):
	"""make the magiciana great"""
	while magicians_name:
		new_name = 'the Great ' + magicians_name.pop().title()
		magicians.append(new_name)

def show_magicians(magicians):
	"""show magician's name"""
	print("magician name: ")
	for name in magicians:
		print(name.title())

magicians_name = ['tom', 'billy', 'tony']
magicians = []

show_magicians(magicians_name)
make_great(magicians_name[:])
show_magicians(magicians)