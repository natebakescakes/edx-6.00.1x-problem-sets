epsilon = 0.01
y = 12345.0
guess = y / 2.0
count = 0

while abs(guess * guess - y) >= epsilon:
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    print (guess)
    count += 1
    
print ('\nNo. of guesses: %d' % count)    
print ('Square root of ' + str(y) + ' is about ' + str(guess))