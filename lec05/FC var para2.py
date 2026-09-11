def print_all(*args):
    for  index, args in enumerate(args):
        print(f"Agrument : {index + 1} ", args)

print_all("kiw", "love", "pink", 3000, True, [9000])