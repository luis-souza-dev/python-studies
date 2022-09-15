age = 20
name = 'Luis'
question = 'What\'s your name?'

print(question)
print('{0} was {1} year old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))


# decimal (.) precision of 3 for float '0.333'
print('{0:.1f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))