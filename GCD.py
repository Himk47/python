def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
print (hcfnaive(8,12))