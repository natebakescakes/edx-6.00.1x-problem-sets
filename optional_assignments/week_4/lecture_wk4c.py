def nfruits(init_fruits, pattern):
    """
    init_fruits: Non-empty dictionary containing initial type of fruit and its 
            quantity initially with Python when he leaves home 
            (length < 10)
            
            e.g. {'A': 1, 'B': 2, 'C': 3}
            
    pattern: String pattern of the fruits eaten by Python on his journey
    
            e.g. 'AABBBBCA'
    
    return: maximum quantity out of the different types of fruits that is 
            available with Python when he has reached the campus.
    """
    
    max_quantity = 0
    working_fruits = init_fruits.copy()
    
    # Loop through string pattern to update fruit quantities
    for i, char in enumerate(pattern):
        assert char in working_fruits.keys() # Make sure that char in initial fruits        
        
        # If character is not last in string pattern
        # Decrement fruit by one, increment other fruits by one
        if i != len(pattern) - 1:
            for key in working_fruits.keys():       
                if char == key:
                    working_fruits[key] -= 1
                else:
                    working_fruits[key] += 1
        # Else if last character in string, just decrement fruit by one
        else:
            working_fruits[char] -= 1
            
    # Find maximum quantity of all fruits at the end
    for key in working_fruits:
        if working_fruits[key] > max_quantity:
            max_quantity = working_fruits[key]     
            
    return max_quantity   
    