#Calculating the amount of money required depending on the number of units and tax

unit = int(input('Enter the number of Units Electricty consumed : '))

if unit <= 50:
    amount = unit * 2.60
    surcharge = 25
elif unit <= 100:
    amount = (50 * 2.60) + ((unit - 50) * 3.25)  
    surcharge = 35
elif unit <=200:
    amount = (50 * 2.60) + (50 * 3.25) + ((unit - 100) * 5.26)
    surcharge = 45
else:
    amount = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + ((unit - 200) * 8.45)
    surcharge = 75

print('Bill Amount is : ' ,amount )
print('Tax Amount is : ',surcharge)
print('Total amount required to pay is : ',amount + surcharge) 