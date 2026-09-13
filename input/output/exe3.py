product_price = float(input("Product Price :"))
tax = product_price * 0.07
total_price = product_price + tax

print(f"Before Tax:{product_price :.2f}")
print(f"Tax :{tax:.2f}")
print(f"After Tax :{total_price:.2f}")