cars = ['GTI', 'Tacoma', 'Crosstrek', 'Tundra', 'Atlas']
print(cars)

print(cars[2])

print(cars[2].upper())




cars[0] = 'Hotwheels'
print(cars)

cars.append('Tonka')
cars.append('GTI')
print(cars)

motorcycles = []
print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('Yamaha')
motorcycles.append('Harley')

print(motorcycles)

print(motorcycles[2])
print(motorcycles[2].upper())
print(motorcycles[0].title())

motorcycles.insert(1, 'Honda')
print(motorcycles)

motorcycles.insert(3, "Indian")
print(motorcycles)

del motorcycles[3]
print(motorcycles)


cars = ['GTI', 'Tacoma', 'Crosstrek', 'Tundra', 'Atlas']

print(cars)
last_owned = cars.pop()



motorcycles = ['ducati', 'honda', 'harley', 'yamaha']

motorcycles.remove('honda')
print(motorcycles)
cars.sort(reverse=True)
print(cars)

print(len(motorcycles))

motorcycles.append('lotus')
print(motorcycles)
print(len(motorcycles))

motorcycles.reverse()
print(motorcycles)
 #index is just another word for position in a list (i.e. [0] [1] [2], etc)

 


