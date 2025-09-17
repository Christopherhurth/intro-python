print("Chris Hurth if_examples A04")
# SECTION 1: Equality
print('SECTION 1: Equality')
print('\n')

print('(A) Demonstrate checking whether two values are equal or not.')
print('\n')

my_number = 17
print("Guess my number!", my_number)
guess_0 = 17
if guess_0 ==17:
    print("my guess is...", guess_0)
    print('Great guess!')
    print('\n')

print('(B) Demonstrate checking for inequality between two values.')
guess_1 = 13
if guess_1 != 17:
    print("you guessed...", guess_1)
    print('Try again...')
    print('\n')
guess_2 = 10
print('(C) Demonstrate checking whether a value is greater than, less than, greater than or equal to, or less than or equal to another value.')
if guess_2 <= 16:
    print("your guess is...", guess_2)
    print('Try higher')
guess_3 = 45  
if guess_3 >= 18:
    print("this guess is...", guess_3)
    print("Try lower.")
print('(D) Demonstrates checking whether a list is empty or not before processing its items.')
print('\n')
rocks = ['granite', 'lava']
if rocks:
    print("the list is not empty")
    for rock in rocks:
        print(rock)
       
rocks = []
if rocks:
    print("This list is not empty")
    for rock in rocks:
        print(rock)
else:
    print('No rocks!')
print('\n'*3)


# SECTION 2: If statements


print('SECTION 2: If statements')
print('\n')

print('(A)Demonstrate the use of if statements to execute code conditionally.')

items =['Audi', 'book', 'rock', 'sand']
car = 'Audi'
print("choose the car.", items)

print('Please enter the car.')
print(car)
for car in items:
    if car == 'Audi':
        print('Great job!')
print('Get ready for the next part!')
print('\n')

print('(B)Demonstrate the use of if-else statements to provide alternative code paths.')

print('\n') 

movie_a = 'superman'
if movie_a == 'superman':
    print('superman movie!')
else:
    print('not a superman movie!')
    
    
movies = ['shawshank redemption', 'green mile', 'stand by me',
                     'life of chuck', 'superman', 'starship troopers', 'the rock', 'batman']

# movies_not_by_SK = ['superman', 'starship troopers', 'the rock']
# for movie in movies:
#     print('-',movie.title())

# for movies_not_by_SK in movies_not_by_SK:
#     if movies_not_by_SK in movies:
#         print(f"Steven King did not write this one: {movies_not_by_SK}")
#     else:
#         Print(f"Steven King wrote all these amazing movies first in book form! {movies_not_by_SK}.")

print('\nBut all of these movies are great add-on to any watch list!\n')
 
print('(C)Demonstrate the use of if-elif-else chains to handle multiple conditions.')
# print('\n') 

movie = "starship troopers"

if movie in [movies]:
    print(f'\n{movie.title()} is based on a Steven King novel.')
elif movie == 'superman':
    print(f'\n{movie.title()} is a super hero movie based on DC comics.\n')
elif movie == 'starship troopers':
    print(f'\n{movie.title()} This is a Sci-fi movie based on a the same title book.')
elif movie == 'the rock':
    print(f'\n{movie.title()} This is an action film starring Sean Connery and Nick cage, not based on a novel.\n')
else:
    print('Movie not found!')


#SECTION 3: Logic operators


print('\nSECTION 3: Logic operators')
print('\n\n\n')
movie_1 = 'superman'
movie_2 = 'batman'
Steven_King = ['shawshank redemption', 'green mile', 'stand by me', 'life of chuck']


print('(A)Demonstrate the use of the logical operators (and) to combine multiple conditions in if statements.')
if movie_1 == 'superman' and movie_2 == 'batman':
    print(f'\n{movie_1.title()}definitely a Superhero movie, not a Steven King novel.')
    
    
print('(B)Demonstrate the use of the logical operators (or) to combine multiple conditions in if statements.')
if movie_1 == 'superman' or movie_2 == 'auqaman':
    print(f'\n{movie_1.title()} Superhero movie!')
    

print('(C)Demonstrate the use of the logical operator (not) to invert the result of the in keyword.')
if movie not in Steven_King:
    print(f'\n{movie.title()} falls into some other SCI-FI genre.')