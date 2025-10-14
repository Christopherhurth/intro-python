# Christopher HurtH- Assignment A07: Funtions, part A:


# Section 1: Basic Functions
print('\nSection 1: Basic Functions')


print('\nA:')
# A: Define and use a function that takes two integers a and b and returns a**b.

# def raising_x_to_y(first_num = 5, second_num = 5):
#    """raising first number by the second"""
#     answer = first_num ** second_num
#     return answer      

def raising_x_to_y(first_num = 5, second_num = 5):
    """raising first number by the second"""
    answer = first_num ** second_num
    return answer   

answer = raising_x_to_y(5 , 2)        
print("-Number anwser is now: ", answer)

answer = raising_x_to_y()        
print("-Number anwser is now: ", answer)


print('\n\nB:')
# B: Define and use a function that takes first and last names as well
#       as a prefix (Mr. Mrs. Ms.) and returns the full name with the proper prefix.

def build_person(first_name, last_name, prefix):
    """Return a dictionary of information about a person."""
    person = f'{prefix.title()} {first_name.title()} {last_name.title()}'
    return person

print(build_person("bob", "jones", "Mr."))


print('\n\nC:')
# C: Run the function above using named arguments that are out of order with 
#       the function definition.

print(build_person(last_name = "jones", prefix= "mr.", first_name= 'bob'))


print('\n\nD:')
# D: Copy and modify the function above to make the prefix optional.

def build_person_op(first_name, last_name, prefix = ""):
    """Return a dictionary of information about a person."""
    if prefix:
        person = f'{prefix.title()} {first_name.title()} {last_name.title()}'
    else:
        person = f'{first_name.title()} {last_name.title()}'
    return person

print(build_person_op("bob", "jones"))
print(build_person_op("bob", "jones", "mr."))


print("\n\nE:")
#  E: Define a function that takes a list as an argument and modifies the list directly in the function. 
#       It should not return a value. Demonstrate that it changes the passed list.

def change_list(my_list):
    my_list.pop()
    
test_list = ['first', 'second', 'third']
print(test_list)
change_list(test_list)
print(test_list)


print("\n\nF:")
#  F: Show what happens when you pass a copy of the list to the function above.

test_list = ['first', 'second', 'third']
print(test_list)
change_list(test_list[:])
print(test_list)




print("\n\n\nSection 2: Complex Arguments\n\n")
# Section 2: Complex Arguments



print('\n\nA:')
# A: Define and use a function that takes a string as the first argument and then an arbitrary number
#       of strings. Create a list by concatenating the first argument to each of the additional arguments.
#       Return the list.

def super_things(prefix, *things):
    """Things that can be super!"""
    results = []
    for thing in things:
        results.append(f'{prefix.title()}{thing.title()}')
    return results

print(super_things('super', '-man', '-women', '-star', '-hero', '-teams', '-ratings', '-foods'))

      
print('\n\nB:')
# B: Define and use a function that takes a string as an argument and additional key / value pairs. 
#       Return a dictionary that contains the first argument with the associated key called 'name'. 
#       The rest of the dictionary should contain the key / value pairs passed in the second argument.

def build_character(name, last, **character_info):
    """Build a dictionary containing everything we know about a fictional charater."""
    character_info['first_name'] = name.title()
    character_info['last_name'] = last.title()
    return character_info

character_profile = build_character( 'montana', 'coggeshall',
                            continent= 'Vuldranni',
                            character_class= 'Bergman',
                            books= 'The Good Guy Series')
print(character_profile)