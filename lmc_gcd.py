from lib2to3.pgen2.token import GREATER


num1 = int(input("Enter :"))
num2 = int(input("Enter :"))

grater = num1 if (num1>num2) else num2 

for i in range(grater+1,1,-1):
    if (num1 % i == 0 and num2%i ==0):
        print("GCD :",i)
        break
    else:
        continue

print(i)        
