alien_0 = {'color': 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print(f"Congratulations, you just earned {new_points} points!")

#below is how you add to an already exisiting dictionary

alien_1 = {'color': 'green', 'points' : 10}

alien_1['x_position'] = 0
alien_1['y_position'] = 25
alien_1['hair color'] = 'red'
alien_1['speediness'] = 'medium'

print(alien_1)


#below is how you add to empty dictionary. use curly braces, not square brackets!

alien_2 = {}

alien_2['speed'] = ('25 mph')
alien_2['weight'] = ('175 lbs')
alien_2['toughness_level'] = 10

print(alien_2)

alien_2['speed'] = ('55 mph')

print(f"The alien has a speed of {alien_2['speed']}!") #Need to use a combination of double and single quotes since if all of one or other would confuse program on where the stop was.


print(alien_1)

print(f"Original position: {alien_1['x_position']}")

alien_1['speediness'] = 'fast' #by changing the value for the speedienss key from "medium" to "fast" the condtional statements below...
								#update accordingly. Keep in mind this needs to be done before the condtionals below or it won't work

if alien_1['speediness'] == 'slow':
	x_increment = 1

elif alien_1['speediness'] == 'medium':
	x_increment = 2

else:
	#this must be a fast alien
	x_increment = 3

#the new posiiton is the old position plus the increment

alien_1['x_position'] = alien_1['x_position'] + x_increment





print(f"New position: {alien_1['x_position']}")




