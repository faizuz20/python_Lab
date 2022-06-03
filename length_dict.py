length=int(input("Enter The Number of Pairs: "))

d={}
for i in range(length):
    name=input("Enter the name:")
    roll_num=input("Enter The roll_num:")
    d.update({name:roll_num})

print(d)
p=""
for i in d.keys():
    p+=i

print(p)

for j in d.values():
    p+=j

print(p)

total_len = len(p)
print(total_len)