def f_value(amt,int,years):
    return amt*((1+(.01*int))**years)
print (f_value(10000,3.5,7))