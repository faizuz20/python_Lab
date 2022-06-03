num1=int(input("Enter:"))
num2=int(input("Enter:"))
fun=lambda x,y:print("Yes!") if num1%num2==0 else print("No!")
print(fun(num1,num2))