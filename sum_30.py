sum=0
for i in range(1,31):
    if i == (10):
        continue
    if i == (20):
        continue
    elif(i%2 == 0):
        sum+=i
        print(i)
    else:
        continue    

print(sum)        
