alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x_position: ' + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
#move the aliens to the right
#move the aliens according to how fast the aliens move
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_position " + str(alien_0['x_position']))