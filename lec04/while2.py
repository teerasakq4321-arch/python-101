import random

print("What you magic number(1 to 100)?")
mynumber = random.randint(1, 100)
guess_round = 1
yourguess = -1

while guess_round < 10 and yourguess != mynumber:
     if guess_round == 9:
        print("You last chance")

     msg = str(guess_round) + ">>"
     yourguess = int(input(msg))
        
     if yourguess > mynumber:
        print("-->too high")
     elif yourguess < mynumber:
        print("-->too low")
     guess_round += 1
    
if yourguess == mynumber:
 print("Yes is my number :", mynumber)
else:
 print("No is my number :", mynumber)