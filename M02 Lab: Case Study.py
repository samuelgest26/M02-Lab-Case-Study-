# Samuel Gest
# M02 Lab: Case Study.py 
# This application asks the user for their name and GPA then decides whether they have made the dean's list or honor roll 

# Asking the user for their last name 
L_Name = input('Enter Last Name or enter ZZZ to quit: ')
# making sure input does not equal ZZZ
while L_Name != 'ZZZ':
    # Asking the user for their first name 
    F_Name = input('Enter First Name: ')
    # Asking the user for their GPA 
    GPA = float(input('Enter GPA: '))
    # if the GPA is greater than 3.5 then they made the Dean's List
    if GPA >= 3.5:
        print('Congrats', F_Name, L_Name,'.', " You have made the Dean's List")
    else:
        # Else if the GPA is greater than 3.25 they have made the honor roll
        if GPA >= 3.25:
            print('Congrats', F_Name, L_Name,'.' " You have made the Honor Roll")
    # Repeating process until ZZZ is entered       
    L_Name = input('Enter Last Name: ')
