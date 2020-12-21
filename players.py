#this section is deailng with slicing. chapter 3 of the python book. 


players = ['david', 'erin', 'riley', 'tucker', 'sherlock', 'random']
print(players[:4]) #this takes a list from the 0 startin point (david) and ends at 3(tucker)

print(players[0:3]) 

print(players[4:]) #this takes a list from the [4] spot (Sherlock) and finishes off the list

print(players[-3:]) #by using a negative in front of the index( position), this will take the last 3 items from the end of the list

print("Here are the first three people who live in the house:")
for player in players[:3]:
	print(player.title())
