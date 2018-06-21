# CTI-110
# P3TLAB-Debugging
# Francicso PolancoDelaRosa
# 6/21/2018

def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

score = int(input('Enter a numeric score: 0 to 100 '))

if score > 89:
        print('You made an A: ')
        print('Your numeric score of',score,'is an A ')
elif score> 79:
    print('You made a B: ')
    print('Your numeric score of',score,'is an B ')         
elif score > 69:
    print('You made a C: ')
    print('Your numeric score of',score,'is an C ')          
elif score > 59:
    print('You made a D: ')
    print('Your numeric score of',score,'is an D ')
elif score > 49:
    print('You made a F: ')
    print('Your numeric score of',score,'is an F ')
else:
        print('invalid')
# program start
main()
