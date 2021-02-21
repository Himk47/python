def soc(value):
    add = 0
    n = 1
    if value > 0:
        for i in range(value - 1):
            add += n ** 3
            n += 1
    else:
        print("The number you entered is negative.")
    print(add)


soc(3)
