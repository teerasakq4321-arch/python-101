def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0

    for digits in num_str:
        total += int(digits) ** num_digits

    return total == number

print(is_armstrong(153))
