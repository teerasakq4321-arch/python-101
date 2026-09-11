num_employees = int(input("Enter number employees :"))


if num_employees < 50:
    print("This is small company")
elif num_employees < 250:
    print("This is medium company")
elif num_employees >= 250:
    print("This is big company")


score = 80

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B") 
elif score >= 70:
    print("Grade c") 
else:
    print("D or F")