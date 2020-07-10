
def finder(files, queries):
    cache = {}
    result = []
    for file in files:
        if file not in cache:
            cache[file] = False
    for each in cache:
        for query in queries:
            if query not in cache:
                if query in each:
                    cache[each] = True
                    result.append(each)
    return result

    # cache = {}
    # result = []
    # for file in files:
    #     if file not in cache:
    #         cache[file] = False
    # for each in cache:
    #     for query in queries:
    #         if query not in cache:
    #             if query in each:
    #                 cache[each] = True
    # for item in cache:
    #     if cache[item] == True:
    #         result.append(each)
    # return result

    # for query in queries:
    #     if query not in cache:
    #         cache[query] = False
    # for item in cache:
    #     for file in files:
    #         if item in file:
    #             cache[item] = True
    # for each in cache:
    #     if each == True:
    #         result.append(file)
    # return result

    # result = []
    # for file in files:
    #     cache[file] = None
    # for file in files:
    #     for query in queries:
    #         if query in file:
    #             cache[file] = True
    # for item in cache:
    #     if cache[item] == True:
    #         result.append(item)
    # return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
