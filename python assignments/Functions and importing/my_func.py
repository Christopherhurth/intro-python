# Christopher Hurth- Assignment A07: Funtions, part B:

#Section 3: Modules
print('\nSection 3: Modules\n')

print("Part 1...")

# Create at least 4 related functions in the module. These can be anything you like, but they should all take at least 2 arguments
#       of some time and return a value based on those arguments.

#funtion #1 of 4

def voltage(i, r): 
    return i * r

#funtion #2 of 4

def resistance(v, i):
    return v / i 
#funtion #3 of 4

def current(v, r):
    return v / r
#funtion #4 of 4

def Resistance_Parallel(*res):
    resistance = 0
    for r in res:
        resistance += 1 / r
           
    return resistance

# print(round(Resistance_Parallel(10, 10, 10), 2))

