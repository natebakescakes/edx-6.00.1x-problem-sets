def flatten(aList):
    result = []
    for elem in aList:
        if type(elem) == list:
            for elem in flatten(elem):
                result.append(elem)
        else:
            result.append(elem)
    return result