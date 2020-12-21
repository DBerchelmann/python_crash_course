requested_toppings = [] #empty list without a user input will produce nothing

if requested_toppings:
	for requested_topping in requested_toppings:
	    print(f'Adding {requested_topping}.')
	print('\nFinished making your pizza!')
else:
	print("Are you sure you want a plain pizza?")


#the below is a way to work in multiple lists while running through differet elements in a loop

our_toppings = ['pepperoni', 'jalapenos', 'onions'
				'extra cheese', 'mushrooms' 'sausage']

their_toppings = ['french fries', 'pepperoni', 'blue cheese', 'balogna', 'jalapenos']

for their_topping in their_toppings:
	if their_topping not in our_toppings:
		print(f"Sorry, we don't have {their_topping}.")
	else:
		print(f"Thank you! Adding {their_topping} to the pizza!")
print('\nYour pizza is now ready!')
