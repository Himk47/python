def unq(values):
    for i in range(len(values)-2):
        if (values[i]!=values[i+1]!=values[i+2]) and (values[i]+values[i+1]+values[i+2]==0):
            print(values[i],values[i+1],values[i+2])
values = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(unq(values))
