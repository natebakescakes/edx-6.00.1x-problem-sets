x = 12345
epsilon = 0.01
step = epsilon ** 2
guesses = 0
ans = 0.0

while (abs(ans ** 2 - x)) >= epsilon and ans <= x:
    ans += step
    guesses += 1
    
print ('guesses = ' + str(guesses))

if abs(ans ** 2 - x) >= epsilon:
    print ('Failed on square root of ' + str(x))
else:
    print (str(ans) + ' is close to the square root of ' + str(x))