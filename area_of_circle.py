# A program to find area of the circle

inpu = input('Enter the Radius type :')
if (inpu == 'float'):
    rad = float(input('Enter The Radius :'))
    area = 3.14*(rad**2)
    print('The area of the Circle will be :',area)
    
if (inpu == 'integer'):
    rad = float(input('Enter The Radius :'))
    area = int(3.14*(rad**2))
    print('The area of the Circle will be :',area)
        
