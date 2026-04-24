# food amount per month 
# flate rent per month
# man 
#electricity  charge per unit 
# electricity  spend per month

food_amount= int(input("enter the food amount:"))
flate_rent= int (input("enter the  amount:"))
charge_unit=int(input("enter the charge per unit:"))
per_man=int(input("enter man:"))
electricity_spend= int(input("enter the spending amount:"))
total_bill= (charge_unit*electricity_spend)
print(total_bill)

output=(food_amount+flate_rent+total_bill % per_man)
print(output)