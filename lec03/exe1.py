number = []
print("กรอกตัวเลข(พิม q เพื่อหยุด)")

while True :
    user_input = input("ตัวเลข :")
    if user_input == "q":
        break
    number.append(float(user_input))

if number :
    average = sum(number) / len(number)
    print(f'ค่าเฉลี่ย : {average}')
else:
    print("ไม่มีข้อมูล")