def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = []
    res = []
    if length < 2:
        return None

    for i in range(length):
        diff = limit - weights[i]
        print(diff)
        if diff in hash:
            print('YES',hash.index(diff))
            res.append(i)
            res.append(hash.index(diff))
            return res
        else:
            hash.append(weights[i])
    
    # print(hash)

    # res = []

    # for x in range(length):
    #     if weights[x] + hash[x][1] == limit:
    #         res.append(x)
    #         res.append(hash[x][0])
    #         print(res)
    #         return res
    #     else:
    #         return None
