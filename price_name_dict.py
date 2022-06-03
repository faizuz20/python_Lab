d={}
choice=input("Enter Y'r Choice:")
num=int(input("Enter number of product's: "))

for i in range(num):
    if choice == "y" or choice == "Y":
        pro=input("Enter the product name:")
        price=int(input("Enter the price:"))
        d.update({pro:price})
    

    elif (choice=="n" or choice=="N"):
        print("OK")

print(d)



