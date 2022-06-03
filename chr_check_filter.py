lst=[]
num=int(input("Enter:"))
for i in range(num):
    n=input("Enter:")
    lst.append(n)

print(lst)

def fun(x):
    lst1 = ['a','b','c','d','e','f']
    for i in lst1:
        if x==i:
            return True

        else :
            return False

filterout = filter(fun,lst)
print(filterout)     
for j in filterout :
    print(j)