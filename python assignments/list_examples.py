# Section 1: Access items in the list

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

# Next step 2

print(cars[0])

# Next step 3

print(cars[-1])

# Next step 4

print(len(cars))

# Section 2: Append, insert, remove

print(cars[0].title())
print(cars)

print(cars[1].title())
print(cars)

print(cars[2].title())
print(cars)

print(cars[3].title())
print(cars)

# Next step 2

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

cars.append('civic')
print(cars)

#next step 3

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

cars.insert(0, 'civic')
print(cars)

#next step 4

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)
 
del cars[1]
print(cars)

# Section 3: Popping and remove value

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

#next step 2

popped_cars = cars.pop(3)
print(popped_cars)

#next step 3

popped_cars = cars.pop(0)
print(popped_cars)

#next step 4

cars = ['viper', 'rivian', 'infinity', 'prius']

del cars[2]
print(cars)

# Section 4: Sorting

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

cars.sort()
print(cars)

#next step 2

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

cars.sort(reverse=True)
print(cars)

#next step 3

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

print("original list:")
print(cars)

print("sorted list:")
print(sorted(cars))

#next step 4

cars = ['viper', 'rivian', 'infinity', 'prius']
print(cars)

print("This is the original list:")
print(cars)

print("This is the reverse sorted list:")
cars.reverse()
print(cars)

















