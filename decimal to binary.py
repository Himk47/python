num=int(input("enter the number "))
bin=str(num%2)
while num!=1:
    num=num//2
    bin = str(num % 2) + bin
print(bin)