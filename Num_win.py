num = int(input("ENter The number of Player's :"))
game=dict()

for i in range(num):
    key = input("Enter The player Name :")
    win = int(input("Enter THe number of Win:"))
    game[key]=win

print(game)    