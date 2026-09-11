hours_work = float(input("Enter the number hours work  :"))
hours_pay_rate = float(input("Enter the hours pay rate  :"))

if hours_work > 40:
   regular_pay = 40 * hours_pay_rate
   overtime_hours = hours_work - 40
   overtime_pay = overtime_hours * (1.5 * hours_pay_rate)
   gross_pay = regular_pay + overtime_pay
   
else:
   gross_pay = hours_work * hours_pay_rate

print(f"You gross pay :" , gross_pay)
  