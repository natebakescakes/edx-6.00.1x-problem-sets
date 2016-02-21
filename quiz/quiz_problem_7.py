def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    intersect, difference = {}, {}
    
    for i in d1.keys():
        for j in d2.keys():
            if i == j: # If common
                intersect[i] = f(d1[i], d2[j])
                
    for i in d1.keys():
        if i not in d2.keys():
            difference[i] = d1[i]
            
    for j in d2.keys():
        if j not in d1.keys():
            difference[j] = d2[j]
            
    return (intersect, difference)