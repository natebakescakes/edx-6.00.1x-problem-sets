x = 1234567
epsilion = 0.01
guesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilion:
    print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    guesses += 1
    
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print ('guesses = ' + str(guesses))
print (str(ans) + ' is close to square root of ' + str(x))