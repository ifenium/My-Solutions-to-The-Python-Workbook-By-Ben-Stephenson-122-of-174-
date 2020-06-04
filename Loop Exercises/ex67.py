'''
Exercise67: AdmissionPrice
A particular zoo determines the price of admission based on the age of the guest. 
Guests 2 years of age and less are admitted without charge. Children between 3 and 12 years of age cost $14.00. 
Seniors aged 65 years and over cost $18.00. Admission for all other guests is $23.00. 
Create a program that begins by reading the ages of all of the guests in a group from the user, 
with one age entered on each line. The user will enter a blank line to indicate that there are no more 
guests in the group.Then your program should display the admission cost for the group with an appropriate 
message. The cost should be displayed using two decimal places.
'''

age = input('Enter your age (press Enter to quit): ')

total = 0

while age != "":
    age = int(age)

    if age <= 2:
        fee = 0
    elif 3 <= age <= 12:
        fee = 14.00
    elif age >= 65:
        fee = 18.00
    else:
        fee = 23.00
    total += fee

    age = input('Enter your age (press Enter to quit): ')
    
print('The Total cost for admitting this person or group is {:.2f}'. format(total))