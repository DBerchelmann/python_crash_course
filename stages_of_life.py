#built a list and the ran through each value and compared against a number of conditions

age_list = [2, 35, 88, 23, 12, 9]

age_list.extend ([99, 1, 25, 14, 3])

age_list.sort()

for age in age_list:

	if age < 2:
		print('this person is a baby')
	elif age >= 2 and age < 4:
		print('this person is a toddler')
	elif age >= 4 and age  < 13:
		print('this person is a kid')
	elif age >= 13 and  age < 20: 
		print('this person is a teenager')
	elif age >= 20 and age < 65:
		print('this person is an adult')
	else:
		print('this person is old')

print(age_list)