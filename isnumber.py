ifnumeric=False
while ifnumeric==False:
    str=input("enter a number:")
    if str.isnumeric():
        print("yes it is a number")
        ifnumeric = True
    else:
        print("no its not a number.try again")
