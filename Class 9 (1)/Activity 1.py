#Checking exam eligibility
att = int(input('What is the percentage of your attendance? : '))
sick = input('Were you sick during the course? Yes/No? : ')

if sick == 'Yes' or sick == 'yes':
    print('You are eligible for the examinations')
elif sick == 'No' or sick == 'no':
    if att >= 75:
        print('You are eligible for the examinations')
    else:
        print('You are not eligible for the examinations')
else:
    print('Enter valid information')