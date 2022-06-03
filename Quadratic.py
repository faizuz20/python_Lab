a = int(input("Enter the value of a :"));
b  = int(input("Enter The value of b :"));
c = int(input("Enter The value of c :"));

D = float((b**2 -4*a*c)**1/2);
root1 = (-b + D)/4*a;
root2 = (-b-D)/4*a;

print("The roots will be :",root1 , root2);
