height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# More practice below using input

dinner_group = input("How many people will be joining you this evening?")

dinner_group = int(dinner_group)

if dinner_group > 8:
    print("\nMy apologies, the wait for tables larger than 8 is two hours at this time")
else:
    print("\nWonderful, we will have you table put together and will seat you in ten minutes.")