#Have nice day for learning python
#And today we start with function docString
def print_max(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    #convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    elif x == y:
        print('x and y are equal')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

help(print_max)
