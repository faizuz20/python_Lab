choice = input('Enter Your choice : C~F or F~C ')
feh = float(input('Enter The temp. in Faharenheit :'))
cel = float(input('Enter THe temp. in celcius'))

if choice == 'C~F':
    temp = (feh-32)*9/5
    print('The converted Temp. is :',temp)
    
elif choice == 'F~C' :
    temp = cel*9/5 + 32
    print('The converted temp to faharenheit :',temp)
        
    
    
    
