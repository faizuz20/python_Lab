string = input('Enter The string :')
length = len(string)
string1 =''

for i in range(length):
    if (i%2 == 0):
        string1+=string[i].upper()
    elif(i%2 != 0):
        string1+=string[i]    
        
print(string1)        
