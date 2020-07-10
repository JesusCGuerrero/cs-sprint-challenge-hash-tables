def has_negatives(a):
    # cache = {}
    # result = []
    # for each in a:
    #     cache[each] = None
    # for item in cache:
    #     if item - (item * 2) in cache:
    #         if item - (item * 2) < 0:
    #             result.append(item)
    # return result

    cache = {}
    result = []
    for each in a:
        if each > 0:
            cache[each] = None
    for number in a:
        if number < 0:
            if number - (number * 2) in cache:
                cache[number - number * 2] = True
    for item in cache:
        if cache[item] == True:
            result.append(item)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))