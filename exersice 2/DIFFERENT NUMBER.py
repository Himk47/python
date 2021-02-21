def numbers(values):
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i]==values[j] and j>i:
                print ("values are equal")
                return

    print ("values are not equal")
numbers([1, 2, 3, 5, 5, 6])