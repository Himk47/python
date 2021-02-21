string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}
comb_list=[]
number=str(input("enter the combination- "))
while len(number)!=2 or (int(number)%10)==0:
    number = str(input("enter the combination again- "))
if len(number)==2:
    l1=string_maps[number[0]]
    l2=string_maps[number[1]]
    for i in l1:
        for j in l2:
            comb_list.append(i+j)
print (comb_list)



