# Samuel Gest
# M02 Lab: Case Study.py 
# This application asks the user for their name and GPA then decides whether they have made the dean's list or honor roll 

L_Name = input('Enter Last Name or enter ZZZ to quit: ')
while L_Name != 'ZZZ':
    F_Name = input('Enter First Name: ')
    GPA = float(input('Enter GPA: '))
    if GPA >= 3.5:
        print('Congrats', F_Name, L_Name,'.', " You have made the Dean's List")
    else:
        if GPA >= 3.25:
            print('Congrats', F_Name, L_Name,'.' " You have made the Honor Roll")
    L_Name = input('Enter Last Name: ')
