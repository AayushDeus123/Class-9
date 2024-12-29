#Customise your ride
print('Select your ride :')
print('1. Bike')
print('2. Car')

o = int(input('Choose from the given rides : '))

#Option 1
if o == 1:
    print('\nWhat is your preferred type of bike?')
    print('1. Motorbike')
    print('2. Stuntbike')
 
    b = int(input('Choose from the given types of bikes : ')) 
    if b == 1:
        print('You have selected Motorbike')
    else:
        print('You have selected Stuntbike')
    
#Option 2        
elif o == 2:
    print('\nWhat is your preferred type of car?')
    print('1. Sedan')
    print('2. SUV')
    
    c = int(input('Choose from the given types of cars :'))
    if  c == 1:
        print('You have selected Sedan')
    else:
        print('You have selected SUV')

else:
    print('Inavalid options')