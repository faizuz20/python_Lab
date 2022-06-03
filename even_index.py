string = input("Enter :")
length =len(string)
string1 = ''

for i in string:
    if(string.index(i)%2 == 0):
        string1+=i

    else:
        continue

print(string1)        
