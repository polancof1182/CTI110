# CTI-110
# P3HW1-Age Classifier
# Francisco PolancoDelaRosa
#6/19/2018

# Write a program that asks a persons age and puts them in a classified group.

choice = 'y'

   
age = int(input('Enter age from 1 to 100: '))
if age == 1: 
          print('Infant')
          
elif age > 1 and age < 13:
          print('Child ')
elif age > 13 and age < 20:
          print('Teenager ')
elif age > 20 and age < 100:
          print('Adult ')
    
else:
    print
    choice = input('Do you want to run the program again?' + 'y or n ')
