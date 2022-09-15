number = 23
guess = int(input('Enter a integer: '))

if guess == number:
    print('correct Guess')
    print('Thanks for trying!')
elif guess < number:
    print('No, its greater than that.')
else: 
    print('No, its smaller than that')
    
print('Done')