ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Luis': 'luis@luis.com',
    'Test': 'test@test.com',
    'Natürlich': 'natürlich@ac.co'
}

print('Swaroop address is: ', ab['Swaroop'])

del ab['Test']

print('\nThere are {} contacts in the address book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name, address))
    
ab['binSpäter'] = 'bin@später.de'

if 'binSpäter' in ab:
    print('bin Später address is {}'.format(ab['binSpäter']))