container=int(input("enter the number of elements: "))
list=[]
for i in range(0,container):
    list.append(int(input()))
number=int(input("enter a number: "))
for n in list:
    if n<number:
        print ("NO")
        break
else:
    print ("YES")