print("Welcome. This program calculates the minimum number of R200, R100 and R50 notes that you would need to pay a given amount.")
money = float(input("Please enter the amount in Rands: e.g 123.12 represents R123.12: "))
denom = 200
remaining = int(money // denom)
money = money % 200

denom2 = 100
remaining1 = int(money//denom2)
money = money % 100

denom3 = 50
remaining2 = int(money // denom3)
money = money % 50

print("Here's the breakdown:")
print(f"R{denom}: {remaining} notes")
print(f"R{denom2}: {remaining1} notes")
print(f"R{denom3}: {remaining2} notes")
print()
print(f"Amount left: R{round(money,2)}")

v = 1350
denom = v // 500
print(denom)






