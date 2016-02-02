running = True
high = 100
low = 0

print ('Please think of a number between 0 and 100!')
    
while running:
    ans = (high + low) / 2
    print ('Is your secret number %s' % ans)
    response = raw_input('Enter \'h\' to indicate the the guess is too high. Enter \'l\' to indicate the guess is too low.  Enter \'c\' to indicate II guessed correctly. ')
    
    if response == 'h':
        high = ans
    elif response == 'l':
        low = ans
    elif response == 'c':
        break
    else:
        print ('Please choose a valid response')
        
print ('Game over. Your secret number was: %s' % ans)