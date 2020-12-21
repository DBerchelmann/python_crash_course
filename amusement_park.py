age = 13
if age < 4:
	print('your admission is free!')
elif age < 18:
	print('your cost is for admission is $15')
else:
	print('your cost for admission is $25')


#when i created a space under age_again, the code was bugging and not returning proper values. When I brought it back together, it worked fine
age_again = 74
if age_again < 4:
	price = 0
elif age_again < 18:
	price = 15
elif age_again < 65:
	price = 20
elif age_again > 65:
	price = 12

print(f"the price of admission is ${price}.")
