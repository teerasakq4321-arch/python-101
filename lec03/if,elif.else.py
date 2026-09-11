

while True:
 inchar = input("Input one character :")

 if inchar >= "A" and inchar <= "Z":
    print("You in put upper case letter :" , inchar)
 elif inchar >= "a" and inchar <= "z":
    print("You in put lower case letter :" , inchar)
 elif inchar >= "0" and inchar <= "100":
    print("You in put number :" , inchar)
 else:
    print("It's not letter or number")
    break