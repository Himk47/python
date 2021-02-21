X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
l1=set()
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Z)):
            if X[i]+Y[j]+Z[k]==target:
                l1.add((X[i],Y[j],Z[k]))
print (l1)