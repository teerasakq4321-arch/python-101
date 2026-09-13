height_cm = float(input("Enter you height in cm:"))
weight = float(input("Enter you weigh :"))
height_m = height_cm * 0.01
bmi = weight / (height_m ** 2)

if bmi >= 25:
    print("You Fat")
elif bmi >= 23:
    print("You Overweight")
elif bmi >= 18.5:
    print("You Normal weight")
else:
    print("ํYou Low weight")