num =int(input('Enter THe number ::'))
count=0

for i in range(1,num + 1):
    if(num % i == 0):
        count+=1
        continue
        
    elif(num % i != 0):
        continue   
        
else:    
    if(count > 2):
        print('The number is not Prime ')
        
        
    elif(count == 2):
        print('The number is prime')        
        
