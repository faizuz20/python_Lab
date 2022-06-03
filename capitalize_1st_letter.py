string = input('Enter the string :')
string1 =''
length = len(string)

for i in range(length) :
        string1 += string[0].upper() 
        
        if (string[i].isspace()):
            string1 += str(string[i+1].upper)
            
print(string1)            
