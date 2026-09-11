NUM_EMPLOYEES = 6

def main():
    hours = [0] * 6
    for index in range(NUM_EMPLOYEES):
        print("Enter your hours ", index + 1  ,":" , sep="",end="")
        hours[index] = float(input())
    pay_rate = float(input("Enter your pay rate :"))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print("You gross pay for employee :", index + 1 , gross_pay, "$" )

main()