print("1 : add ")
print("2 : subtract")
print("3 : multiply ")
print("4 : divide")


operation_select = int(input(" select operation(1-4) :"))
if operation_select not in range(0,5):
    print("Error : invalid operation select")
else:
   num_1 = float(input("Enter you first number :"))
   num_2 = float(input("Enter you second number :"))
   if operation_select == 1:
         result = num_1 + num_2
         print("You answer :" , result)
   elif operation_select == 2:
         result = num_1 - num_2
         print("You answer :" , result)
   elif operation_select == 3:
         result = num_1 * num_2
         print("You answer :" , result)
   elif operation_select == 4:
      if num_2 == 0:
         print("Error : calcuraltion fail")
      else:
         result = num_1 / num_2
         print("You answer :" , result)
          
               
       
    


