def ndigits(x):
    """
    Function that returns the no. of digits in a number recursively
    Takes 1 parameter that is an integer and can be either positive or negative
    """
    if abs(x) == 0:
        return 0
    else:
        return 1 + ndigits(abs(x) / 10)
