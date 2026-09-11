
string_input = input("Enter you string :")

String_storage = ""
vowels = "aeiouAEIOU"

for char in string_input:
    upper_char = char.upper()
    if upper_char in vowels:
        String_storage += "*"
    else:
       String_storage += upper_char

print("The modified is " , String_storage)