num = int(input('Enter The Number :'))
first_num = num // 10
second_num = num % 10

if(first_num%second_num == 0.0):
    print(' divisible ')
    
elif(first_num%second_num != 0.0):
    print('Not Devisible ')    
