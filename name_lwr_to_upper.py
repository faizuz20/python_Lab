s=input()
length=len(s)
l1=list(s)
new=""
new+=s[0].upper()
for i in range(1,length):
    if(l1[i]==" "):
        new+=" "
        l1[i+1]=l1[i+1].upper()

    else:
        new+=l1[i]

print(new)            