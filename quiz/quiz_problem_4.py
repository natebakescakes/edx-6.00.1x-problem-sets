def isPalindrome(aString):
    if len(aString) == 0:
        return True
    elif aString[0] != aString[-1]:
        return False
    else:
        return isPalindrome(aString[1:-1]) and True