import string

def remove_symbols(input):
    return input.lower().translate(str.maketrans('','', string.punctuation)).replace(' ','')

def reverse(something):
    return something[::-1]

def is_palindrome(something):
    return something == reverse(something)

something = input('Enter something: ')
if is_palindrome(remove_symbols(something)):
    print('Yes, it is palindrome')
else:
    print('No, it isn\'t palindrome')