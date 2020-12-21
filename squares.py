squares = []
for value in range(1, 11):
	
	squares.append(value ** 2)

print(squares)

circles = []
for value in range(4, 24):
	circle = value ** 2
	circles.append(circle)

print(circles)


digits = [1, 2, 4, 6, 4, 7, 1, 9, 6]

print(sum(digits)) #other ways to go about this would be max(digits) or min(digits)

#The following is list comprehension for doing squares

squares = [value ** 2 for value in range(1, 13)]
print(squares)


cubes = [value ** 3 for value in range(1, 11)]
print(cubes)