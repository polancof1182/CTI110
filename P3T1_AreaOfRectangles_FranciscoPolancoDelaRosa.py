# CTI-110
# P3T1-Area of Rectangle
# Francisco PolancoDelaRosa
# 6/19/2018

# Write a program that will calculate the length and width of two rectangles.
# Program should tell user which rectangle has the greater area, or equal area.
# Get dimensions of rectangle 1.
length1 = int(input('Enter the length of rectangle1: '))
width1 = int(input('Enter the width of rectangle1: '))
#Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle2: '))
width2 = int(input('Enter the width of rectangle2: '))

# Calculate the areas of area of rectangles 1 and 2.
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    print('Rectangle1 has the greater area. ')
elif area2 > area1:
    print('Rectangle2 has the greater area. ')
else:
    print('Both have the same area. ')

