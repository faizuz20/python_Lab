start = int(input('Enter :'))
stop = int(input("Enter :"))
count=0

for i in range(start,stop+1):
    count = 0
    for j in range(1,i+1):
        if(i%j ==0):
            count+=1
        else :
            continue

    if (count==2):
        print(i)

    elif(count>2):
        print(i , 'is not prime')  
    
