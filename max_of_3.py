n=int(input("Enter The total numbers"))
tup=()
for i in range(1,n+1):
    num=int(input("Enter :"))
    tup+=num,

print(tup)

def max_of_3(s):
    Q=0
    Q=max(s)

    return Q

print("The max of the 3 numbers will be:",max_of_3(tup))
