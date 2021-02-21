def sq(values):
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j and j > i:
                product = values[i] * values[j]
                print(product)
                if product % 2 != 0:
                    print("true")
                    return
    print("false")


sq([2,7,3 ])
