company_1 = input("Name of the first company: ")
ini_1 = float(input("Initiation fee of first company e.g. 256.60 means R256.60: "))
prem_1 = float(input("Basic premium of first company e.g. 256.60 means R256.60: "))
percent_1 = int(input("Loading percentage of first company e.g. 80 means 80 percent: "))

print("")

company_2 = input("Name of the second company: ")
ini_2 = float(input("Initiation fee of second company e.g. 256.60 means R256.60: "))
prem_2 = float(input("Basic premium of second company e.g. 256.60 means R256.60: "))
percent_2 = int(input("Loading percentage of second company e.g. 80 means 80 percent: "))
print("_" * 30)
print("Info | Company 1 | Company 2")
print("_" * 30)
print(f"Name | {company_1} | {company_2} ")
print(f"Init fee | {ini_1} | {ini_2} ")
print(f"Premium | {prem_1} | {prem_2} ")

premload_1 = (((percent_1)/(100)) * (prem_1)) + (prem_1)
premload_2 = (((percent_2)/(100)) * (prem_2)) + (prem_2)

print(f"Premium loaded | {premload_1} | {premload_2} ")

print("_" * 30)
