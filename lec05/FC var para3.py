def display_info(**kwargs):
    for key , value in kwargs.items():
        print(f'{key} : {value}')

display_info(name="kiw", age=18, city="bangkok")