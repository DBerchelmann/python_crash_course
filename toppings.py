requested_topping = 'mushrooms'

if requested_topping != 'mushrooms':
	print('Hold the anchovies!!')
else:
	print("Now that's how you make a pizza!")

#to test this out, change out the topping in the definition at the top


#for whatever reason, the code below doesn't spit out a true or false in sublime, however, when run...
#...in the terminal, it runs correctly producing a "true" statement
these_toppings = ['jalapeno', 'pineapple', 'ham', 'pepperoni']

'jalapeno' in these_toppings

print('\n') #this adds a space between blocks of code

more_toppings = ['mushrooms', 'cheese']

more_toppings.append ('onions')

print(more_toppings)
print('\n')
if 'mushrooms' in more_toppings:
	print('Adding mushrooms')
if 'cheese' in more_toppings:
	print('Adding cheese')
if 'onions' in more_toppings:
	print('Adding onions')



print("\nFinished making your pizza!")