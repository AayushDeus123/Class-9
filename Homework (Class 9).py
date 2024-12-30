#10 to 20 age group
grade = int(input('Enter your grade : '))
age = int(input('Enter your age : '))
if grade == 10:
    print('')
    if age <= 20 and age >= 10:
        print("You are eligible to be enrolled in Raj's class")
    else:
        print("You are not eligible to be enrolled in Raj's class")
else:
    print("You are not eligible to be enrolled in Raj's class")