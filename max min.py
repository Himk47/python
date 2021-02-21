def maxmin(list):
    l = list[0]
    s = list[0]
    for num in list:
        if num > l:
            l = num
        elif num < s:
            s = num
    print("largest number=", l, "smallest number=", s)


maxmin([1,2,3,4,5,6,7,8,9,10])
