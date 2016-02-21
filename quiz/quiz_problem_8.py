def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    (list) -> int
    """
    Lcopy = L[:]
    
    for letter in Lcopy:
        if not f(letter):
            L.remove(letter)
            
    return len(L)