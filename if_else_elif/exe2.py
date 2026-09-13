year = int(input("Enter you year (A.D.) :"))
if year % 4 == 0 and ( year % 400 == 0 or year % 100 != 0):
    print("This Leap year")
else:
    print("This not Leap year")