print("Welcome to AcmeGym membership calculator.")

opmode = input("Enter the operation mode (either 'Budget or Info'): ").capitalize()

if opmode != "Budget" and opmode != "Info":
    print("Unknown operation mode: " + opmode + " Exiting...")
    exit()

if opmode == "Budget":
    budget = float(input("Enter your budget in rands e.g. 2000 means R2000: "))

    if budget >= 1500:
        print("You can afford the Premium package")
        if 150 <= budget % 1500:
            print("You can also add on swimming pool accsess")
    elif budget >= 500:
        print("You can afford the Access package")
        if 150 <= budget % 500:
            print("You can also add on swimming pool access")
    elif budget >= 220:
        print("You can afford the Easy package")
    else:
        print("No packages available with this budget: R" + str(budget) + "")
else:
    print("Packages: R1500 for Premium; R500 for Access; R220 for Easy; Add R150 for pool access")


