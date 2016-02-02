def fact_i(n):
    """
    assumes that n is an int > 0
    returns n!
    """
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
    
def fact_r(n):
    """
    assumes that n is an int > 0
    returns n!
    """
    
    if n == 1:
        return n
    
    return n * fact_r(n-1)
    
