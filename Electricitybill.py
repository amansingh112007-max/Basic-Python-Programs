# 1. Rename the function (e.g., get_base_charge)
def get_base_charge(k):
    if k == 2:
        base_charge = 500
    elif k == 5:
        base_charge = 700
    elif k == 7:
        base_charge = 1000
    else:
        base_charge = 0
    return base_charge

def calculate_bill(load_val, units_val):
    # 2. Call the updated function name here
    base_charge = get_base_charge(load_val)
    
    if units_val <= 100:
        total_bill = base_charge + (units_val * 5)
    elif units_val <= 200:
        total_bill = base_charge + (units_val * 7) 
    elif units_val <= 300:
        total_bill = base_charge + (units_val * 10)
    else:
        total_bill = base_charge + (units_val * 15) 
        
    return total_bill

print("...........Electricity Bill Calculator..........")
load_val = int(input("Enter the kWh (2, 5, or 7): "))
units_val = int(input("Enter the number of units consumed: "))
print("...........Your Monthly Bill.............")
print("Load:", load_val, "kWh")
print("Units Consumed:", units_val, "units")
bill = calculate_bill(load_val, units_val)
print("The total electricity bill is:", bill, "Rs")