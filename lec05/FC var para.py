def find_max(*args):
    if not args:
        return None
    Max_value = args[0]
    for number in args:
        if number > Max_value:
           Max_value = number
    return Max_value

result = find_max()

print(f"The Max value is" , result)