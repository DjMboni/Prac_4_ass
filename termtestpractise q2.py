#
print("Welcome to AcmeRestuarant Manager")
opmode = input("Enter the operation mode e.g 'V' or 'S': ").upper()



if opmode == "V":
    stock = int(input("Enter the number of items in stock: "))
    usage = int(input("Enter the daily usage: "))
    if stock < 0 or usage <= 0 or stock < usage:
        print("Invalid stock [" + str(stock) + "] and/or usage [" + str(usage)  +"]  values ")
        exit()
    days_left = stock // usage

    print("Your stock will last approximately" + str(days_left) + "days")

    if days_left < 3:
        print("Warning: only " + str(days_left) + " stock left!")

elif opmode == "S":
    price = float(input("Enter per item in rand: "))
    sold = int(input("Enter the number of items sold: "))
    earnings = price * sold
    if sold >= 50:
        earnings = earnings - (earnings * .15)
    print("Earnings for the day : R" + str(earnings) + "")

print("End of the program")

