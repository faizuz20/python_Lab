n=int(input())
num_lst=()

for i in range(n):
    number=int(input())
    num_lst+=number,

for i in num_lst:
    i=str(i)
    if len(i)==10:
        if i[0]=='7' or i[0]=='8' or i[0]=='9':
           for j in (str(i)):
               if 65< ord(j)<122:
                   print("NO")

    
        else:
             print("No")     

    else:
        print("NO")
