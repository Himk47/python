lst = []
n = int(input("enter the number of element-"))
for x in range(n):
    lst.append(int(input()))
print(lst)
lst.pop(0)
print("first item removed-", lst)
