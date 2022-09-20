import string

def check_symbols(str):
    forbidden = ('!',',','.',':',';','\\','/','*',' ')
    forbidden_index = -1
    check_str = str[:]

    for symbol in forbidden:
        forbidden_index = check_str.find(symbol)
    if forbidden_index > -1:
        print('check_str', check_str)
        print('fi', forbidden_index)
        print('str[0 : forbidden_index : ]', str[0 : forbidden_index : ])
        print('str[forbidden_index + 1 : :]', str[forbidden_index + 1 : :])
        check_str = str[0 : forbidden_index : ] + str[forbidden_index + 1 : :]
    return check_str

def reverse(something):
    return something.translate(str.maketrans('','',string.punctuation))[::-1]

def is_palindrome(something):
    return something.translate(str.maketrans('','',string.punctuation)) == reverse(something)

something = input('Enter something: ')
if is_palindrome(something):
    print('Yes, it is palindrome', something, ' ', reverse(something))
else:
    print('No, it isn\'t palindrome', something.translate(str.maketrans('','',string.punctuation)), ' ', reverse(something))