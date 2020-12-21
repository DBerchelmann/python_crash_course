person = { 'first name': 'David', 'last name': 'Smith', 'age': 32, 'city': 'Sweeney'}

for name in person.items():
	print(name)

person.update({'middle name': 'Luis'})

print(person)

for name in person.items():
	print(name)
	