## Section 1: looping through lists
# Define a list of at least 6 strings

science_fiction_movies =['starship troopers', 'star wars', 'star trek', 'i, robot', 'lucy', 'eagle eye' ] 

# Demonstrate looping through the list with a for loop. Print each item on it's own line.

for science_fiction_movie in science_fiction_movies:
    print(science_fiction_movie.title())

# Demonstrate looping through the list with more than one statement inside the loop.

print(f"{science_fiction_movie.title()},\nGood sci fi movies to watch." )

# Demonstrate executing code outside of the loop once it terminates.

print("What would you recommend?") 

## Section 2: The range() function.
# Print a list of integers 1 through 8 using the list() and range() functions.
print('\n')
numbers = list(range(1,9))
print(numbers)
# Print the integers 1 through 5 using the range() function to control a for loop.
for value in range(1,6):
    print(value)
# Create and print a list called every_third that contains every third number between 1 and 25.
for values in range(2,26,3,):
    print(values)
# Use the range function to create a list of the cubes of integers 1 through 10. Print the list.
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
# Use a list comprehension to create a list of integers 1 through 10 divided by 2. Print the list.
# divide2 = []
# for value in range(1, 11):
#     divide2.append(value/2)

# print(divide2)

divide = [value/2 for value in range(1,11)]
print(divide)
## Section 3: Slicing a list.
# Create a list of 6 strings to use for each of the following:
books = ['bobiverse', 'good guys', 'bad guys', 'grim guys', 'the wandering inn', 'harry potter']

# Print a slice of the list containing the first 3 elements.
print('\n')
print(books[0:3])

# Print a slice of the list containing the last 3 elements. Do this by ommiting the stop value.
print('\n')
print(books[3:])
# Print a slice of the last 3 elements in the list using a negative index.
print('\n')
print(books[-3:])
# Use a slice to control a for loop that prints the middle 4 elements of your list.
print('\n')
print(books[1:5])

## Section 4: Making a copy of a list.

# Create code that demonstrates assigning my_list = your_list does not make a copy.
print('\n')
my_list = ['one', 'two', 'three', 'four']
other_list = my_list 
print(my_list)
other_list.append('five')
print(my_list)

# Create code that demonstrates how to use the slice operation to create a copy of a list, and show that it actually made a copy.
print('\n')
my_list = ['one', 'two', 'three', 'four']
other_list = my_list[:]

my_list.append(-1)
other_list.append(-4)

print("\nnow adding a first negative.")
print(my_list)

print("\nnow adding a last negative.")
print(other_list)

## Section 5: Tuples

print('\n')
# Create and print a tuple of 2 values.
matrix = (100, 200)
print(matrix[0])
print(matrix[1])
# Create and print a tuple of only one value.

print('\n')
neo = (1)
print(neo)
# Create and print a tuple of more than 2 values.

print('\n')
trinity = (1,2,3,4,5,6)
print(trinity) 
# Use a for loop to access and print each item in your tuple that has more than 2 values.
print('\n')
ships = (10, 11, 12, 13)
print("\nMany values tuple:")
for ship in ships:
    print(ship)
    