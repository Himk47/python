lst = []
n = int(input("enter the number of element: "))
for x in range(n):
    lst.append(input())
f = False
for i in lst:
    if int(i) % 15 == 0:
        print(i, end=" ")
        f = True
if not f:
    print("none")
