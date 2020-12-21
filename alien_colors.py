alien_color = ['green', 'red', 'yellow']
if 'green' in alien_color:
	print('you just earned 5 points!')

print('\n')

alien_color = ['blue', 'orange', 'red', ] #this set ran through each item in the list
for color in alien_color:
	if color == 'blue':
		print('\nplayer earns 5 points!')
	else:
		print('\nyou just lost 589 points!')

alien_colors = ['green', 'purple', 'yellow', 'brown']
for color in alien_colors:

	if color == 'green':
		print("earned 5 points")
	elif color == 'purple':
		print("earned 10 points")
	elif color == 'yellow':
		print("earned 15 points")
	else: 
		print("you need some color")
