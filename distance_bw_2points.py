dimension  = input('Enter The Dimension 2D or 3D :')

if dimension == '2D':
    x1=float(input('Enter The x1 :'))
    x2 = float(input("Enter The value of the x2"))
    y1 = float(input('Enter The Value of the y1 :'))
    y2 = float(input('Enter The value of y2 :'))
    
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**1/2
    print('The Distance b/w X and Y is ',dist )
    

if dimension == '3D' :
    x1=float(input('Enter The x1 :'))
    x2 = float(input("Enter The value of the x2"))
    y1 = float(input('Enter The Value of the y1 :'))
    y2 = float(input('Enter The value of y2 :'))
    z1 = float(input('Enter The Value of z1 :'))
    z2 = float(input('Enter The value of z2 :'))
    dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1))**1/2
    print('The Distance b/w X and Y is ',dist )    
    
    
