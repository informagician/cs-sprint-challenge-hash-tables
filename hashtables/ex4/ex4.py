def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # to power of two

    hash = {}

    for item in a:
        if item**2 in hash:
            hash[item**2] += 1
        else:
            hash[item**2] = 1
    
    result = []
    for item in hash:
        if hash[item] == 2:
            result.append(math.sqrt(item))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
