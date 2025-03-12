print("Welcome user. This program helps you determine your weight rating using the BMI method.")

weight = float(input("Please enter your weight in e.g.87.7 means 87.7kg: "))
if not 0 < weight < 200:
    print("Weight provided is out of range (>0kg and <= 200kg). Exiting...")
    exit()

height = float(input("Please enter your height in metres e.g. 2.1 means 2.1 metres: "))
if not 0 < height < 3:
    print("Height provided is out of range (>0m and <=3m). Exiting...")
    exit()

bmi = weight / (height**2)
ideal_weight = 20 * (height**2)

if bmi <= 16:
    print(f"Your BMI is {bmi} and you are Severely Underweight")
    print(f"Your ideal weight is {ideal_weight}kg")
    weight_def = ideal_weight - weight
    print(f"You need {weight_def}kg to gain")

elif  16 < bmi <= 18.5:
    print(f"Your BMI is {bmi} and you are Underweight")
    print(f"Your ideal weight is {ideal_weight}kg")
    weight_def = ideal_weight - weight
    print(f"You need {weight_def}kg to gain")

elif 18.5 < bmi <= 25.0:
    print(f"Your BMI is {bmi} and you are Normal")
    print(f"Your ideal weight is {ideal_weight}kg")
    weight_def = ideal_weight - weight
    print(f"You need {weight_def}kg to gain")
    exit()

elif 25.0 < bmi <= 30.0:
    print(f"Your BMI is {bmi} and you are Overweight")
    print(f"Your ideal weight is {ideal_weight}kg")
    weight_surp = weight - ideal_weight
    print(f"You need {weight_surp}kg to lose")
    exit()

elif bmi> 30.0:
    print(f"Your BMI is {bmi} and you are Obese (sorry)")
    print(f"Your ideal weight is {ideal_weight}kg")
    weight_surp = weight - ideal_weight
    print(f"You need {weight_surp}kg to lose")
    exit()


print()
print("THE END")



