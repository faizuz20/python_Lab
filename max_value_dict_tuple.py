d={}
n=int(input("Enter The Number pairs:"))

for i in range(n):
    k=input("Enter The key:")
    tup=()
    for j in range(2):
        num=int(input("Enter Num:"))
        tup+=num,

    d.update({k:tup})

print(d)

for i in d.values():
    print(max(i))
    