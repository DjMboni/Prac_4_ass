print("Welcome. This program helps you calculate your fuel bill for a car with a given fuel consumption rate and the distance it has travelled.")
print("-"*15)
print()

fuelusage100 = float(input("Insert the fuel consumption rate of the vehicle in litres per 100km e.g. 12.2 means 12.2 litres per 100km: "))
print()

dist = float(input("Insert the total distance travelled by the vehicle in km e.g. 786.7 means 786.7km: "))
print()

fuelprice = float(input("Insert the price of fuel in rands per litre e.g. 35.2 means R35.20 "))

fuelusage = fuelusage100 / 100

total = fuelusage * fuelprice * dist

print("-"*15)
print()
print()
print(f"The total fuel bill for this vehicle is: R{round(total,5)}")


