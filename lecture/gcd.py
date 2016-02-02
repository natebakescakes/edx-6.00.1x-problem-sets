def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    higher = max(a, b)
    lower = min(a, b)
    test = min(a, b)
    
    while test > 0:
        if higher % test == 0 and lower % test == 0:
            return test
        test -= 1