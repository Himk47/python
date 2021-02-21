lst = []
n = int(input("enter the number: "))
for x in range(n):
    lst.append(input("enter the digits one by one: "))
print(lst)
lst1 = []
for z in lst:
    if int(z) > 0:
        lst1.append(z)
print(lst1)
