def nfruits(fruits,pattern):
    #fruits: is the stock of fruits that python has
    #pattern is the fruits that python ate
    fruitsate = list(pattern) #generate a list with the fruits that python ate
    total = len(fruitsate)
    for pos in range(total-1):
        fruits[fruitsate[pos]] = fruits.get(fruitsate[pos], 0) -1 #minus the fruits
        for fruit2 in fruits.keys(): # add new fruits
            if fruit2 != fruitsate[pos]:
                fruits[fruit2] = fruits.get(fruit2, 0) + 1
    fruits[fruitsate[total-1]] = fruits.get(fruitsate[total-1], 0) -1
    result = [(v, k) for k, v in fruits.items()] #generate a tuple with the fruits in the stock
    result.sort(reverse=True) #sort the fruits in order to get the maximum stock
    return result[0][0] #return the maximum stock

