def print_max(a, b):
    '''Prints the maximum of two numbers.
     The two values must be integers.'''
    a = int(a)
    b = int(b)

    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')


print_max(1, 3)
print(print_max.__doc__)
