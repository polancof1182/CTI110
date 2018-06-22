# CTI-110
# P3HW2-Software Sales
# Francisco PolancoDelaRosa
# 6/21/2018


# write a program that calculates discount of number of packages purchased
# program will display total cost with discount applied
# get input from the user

quantity = int(input('Enter a quantity from 10 to 100 '))


softwareCost =float(input('Enter the total cost is '))


totalSale = softwareCost * quantity

if quantity > 10 and quantity < 19:
       print('SoftwareCost - .10 ')
       print('Total sale',totalSale - .10)
        
elif quantity > 20 and quantity < 49:
        print('SoftwareCost - .20 ')
        print('Total sale',totalSale - .20)    
elif quantity > 50 and quantity < 99: 
        print('SoftwareCost - .30 ')
        print('Total sale',totalSale - .30)     
elif quantity > 100:
        print('SoftwareCost - .40 ')
        print('Total sale',totalSale - .40)
    
else:
        print('invalid')
    
