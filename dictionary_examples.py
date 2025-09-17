# Section 1: Dictionaries
print('\nSection 1: Dictionaries\n')

# (A) Demonstrate creating a dictionary of items, with strings for keys and values.
print('\n(A) Demonstrate creating a dictionary of items, with strings for keys and values.\n')


elements_0 = {'h': 'hydrogen',
            'c': 'carbon',
            'o':'oxygen', 
            'n':'nitrogen',
            'ar': 'argon',
            'ne': 'sodium'
            }

print(elements_0)

# # (B) Demonstrate adding to the dictionary above.
print('\n(B) Demonstrate adding to the dictionary above.\n')


elements_0['fe'] = 'iron'
print(elements_0)


# # (C) Demonstrate updating an existing value in the dicionary above.
print('\n(C) Demonstrate updating an existing value in the dicionary above.\n')

elements_0['ne'] = 'neon'
print(f"wrong name for Ne")
print(f"Correction for the element Ne is {elements_0['ne']}.\n")


# # Demonstrate removing a key / value pair from the dictionary.
print('\n(D) Demonstrate removing a key / value pair from the dictionary.\n')

del elements_0['ne']
print(elements_0)

# #(E) Demonstrate accessing a value in the dicionary.
print('\n(E) Demonstrate accessing a value in the dicionary.\n')

print(elements_0['h'])


# #(F) Demonstrate accessing a value with the .get() method.
print('(F)Demonstrate accessing a value with the .get() method.\n')

non_gases= elements_0.get('c', 'lead has not been added.')

print(non_gases)


# #(G) Demonstrate using the .get() method to return "Value not found" accessing a non-existent key.
print('(G)Demonstrate using the .get() method to return "Value not found" accessing a non-existent key.\n')

heavy_metals = elements_0.get('pb', 'Value not found.')

print(heavy_metals)


# # Section 2:
print('\n\nSection 2:\n\n\n')


# # (A) Demonstrate accessing all of the keys in a dictionary. (loop through them)
print('(A) Demonstrate accessing all of the keys in a dictionary. (loop through them)\n')

for element_formula in elements_0.keys():
    print(element_formula.title())


# # (B) Demonstrate accessing all of the values in a dictionary. (loop through them)
print('\n\n(B) Demonstrate accessing all of the values in a dictionary. (loop through them)\n')

for element_name in elements_0.values():
    print(element_name.title())


# # (C) Demonstrate accessing all of the key / value pairs with a for loop.
print('\n\n(C) Demonstrate accessing all of the key / value pairs with a for loop.\n')

for element_formula, element_name in elements_0.items():
    print(f"{element_formula.title()} is the formula for {element_name.title()}\n")


# # (D) Demonstrate accessing all of the values in a dictionary sorted by key.
print('(D) Demonstrate accessing all of the values in a dictionary sorted by key.\n\n')

for element_formula in sorted(elements_0.keys()):
    print(f"{element_formula.title()}, are some of the most common elements!\n")


# # Section 3:
print('\n\nSection 3:\n\n\n')


# # (A) Create a dictionary of dictionaries.
print('(A) Create a dictionary of dictionaries.\n')


elements_1 = {
    'noble gases': {
        'he' : 'helium',
        'ne' : 'neon',
        'ar' : 'argon',
        'kr' : 'krypton',
        'xe' : 'xenon',
        'rn' : 'radon',
        'og' : 'oganesson'
    },
    
    'other natural gases' :{
        'h' : 'hydrogen',
        'n' : 'nitrogen',
        'o' : 'oxygen',
        'f' : 'fluorine',
        'cl': 'chlorine'            
    },
}

elements_2 = {
     'helium' : {
         'symbol': 'he',
         'type': 'noble'
     },
      'neon' : {
         'symbol': 'ne',
         'type': 'noble'
     }
    
}

for name, data in elements_2.items():
    print(name,':\n')
    print('\tSymbol:',data['symbol'])
    print('\tType:',data['type'])
    
print(elements_2['helium']['symbol'])


# # (B) Demonstrate accessing items in the dictionary of dictionaries.
print('(B) Demonstrate accessing items in the dictionary of dictionaries.\n')


print(elements_1['noble gases']['he'],'\n')


# # (C) Create a list of dictionaries.
print('\n(C)Create a list of dictionaries.\n')

element_list = [elements_0, elements_1]


# # (D) Demonstrate accessing items in the list of dictionaries.
print('(D) Demonstrate accessing items in the list of dictionaries.\n')

# print(element_list[0])
print(element_list[0]['o'])



