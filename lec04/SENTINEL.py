keep_going = 'y'
while keep_going == 'y':
    item_cost = float(input("Enter the item's wholesale cost :"))
    retail_price = item_cost * 2.5
    print(f"Retail Price is :", retail_price)
    keep_going = input('Do you want to calculater another' 'Retail_price(Enter y for yes) :' )