current_users = ['billy', 'alan', 'charlie', 'amy', 'bob']

new_users = ['Billy', 'Bob', 'a', 'b', 'c']

for name in new_users:
    if name.lower() in current_users:
	    print(name.title() + " has been taken.")
    else:
	    print(name.title() + " can be used.")