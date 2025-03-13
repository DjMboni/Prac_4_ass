print("Welcome. This program calculates the cost of your energy usage.")

units_used = float(input("Please enter your energy usage in kWh e.g. 120.55 represents 120.55kWh: "))
plan = input("Enter your tariff plan (either 'lifeline' or 'domestic'): ").lower()

if plan == "lifeline":
    if 25 >= units_used:
        cost = 0
        print(f"On the lifeline tariff plan, the total cost for  {units_used}kWh will be R{cost}")
    elif 350 >= units_used:
        cost = ((units_used - 25) * 1.1628)
        print(f"On the lifeline tariff plan, the total cost for  {units_used}kWh will be R{cost}")
    elif units_used > 350:
        cost = 377 + ((units_used - 350) * 2.3444)
        print(f"On the lifeline tariff plan, the total cost for  {units_used}kWh will be R{cost}")
    exit()

elif plan == "domestic":
    if 600 > units_used:
        cost = units_used * 1.9280
        print(f"On the domestic tariff plan, the total cost for  {units_used}kWh will be R{cost}")
    elif units_used > 600:
        cost = 1156.8 + (units_used - 600) * 2.3444
        print(f"On the domestic tariff plan, the total cost for  {units_used}kWh will be R{cost}")
    exit()

