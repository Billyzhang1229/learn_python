sandwich_orders = ['tuna sandwich',
                   'pastrami sandwich',
                   'Fried egg sandwich',
                   'pastrami sandwich', 
                   'sausage sandwich'
                   'pastrami sandwich',]

print("Sorry we don't have any pastrami sandwich left.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made you a " + sandwich.title() + '.')

print("All sandwiches are finished.")
for sandwich in sandwich_orders:
    print(sandwich.title())