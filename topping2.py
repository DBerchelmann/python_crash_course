requested_toppings = ['jalapeno', 'pineapple', 'ham', 'pepperoni']

for requested_topping in requested_toppings:
	print(f"Adding {requested_toppings}.")

print('\nFinished making your pizza!')

requested_toppings = ['jalapeno', 'green peppers', 'pineapple', 'ham', 'pepperoni']


for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':

		print("Sorry, we are out of Green Peppers! TRY SOMETHING ELSE :)")
	else:
		print(f'Great topping choice! Adding {requested_topping.title()} to your order.')

print('\nFinished making your pizza!')


