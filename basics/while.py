number = 23
running = True

while running:
    guess = int(input('Enter a integer'))
    if guess == number:
        print('Congrats, you got it!')
    elif guess < number:
        print('Sorry, that was to low')
    else:
        print('Sorry, that was to high')
        
    tryAgain = input('Do you want to give it another go?')
    
    if tryAgain != 'y':
        running = False
else:
    print('The while loop is over')
    
    print('Last guess was', guess)