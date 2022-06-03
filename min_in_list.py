lst = []
lst = eval("Enter the Values of the List :")
length = len(lst)    
for i in length:
    if lst[i] < lst[i+1]:
        continue
        
    else:
        print('The smallest number is :',lst[i])
            
                
