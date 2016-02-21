def dotProduct(listA, listB):
    sum = 0
    for i in range(len(listA)):
        sum += listA[i] * listB[i]
    return sum