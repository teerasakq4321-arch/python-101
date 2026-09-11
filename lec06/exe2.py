inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            break

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def find_most_expensive(inventory):
    if not inventory:
       return None
    most_expensive_item = inventory[0]
    for item in inventory:
        if most_expensive_item[2] > item[2]:
           most_expensive_item = item
    return most_expensive_item[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
           item[1] = quantity
           item[2] = price
           return
    inventory.append([item_name, quantity, price])

# Action 1: ขาย Banana ไป 20 ชิ้น
update_inventory(inventory, "Banana", 20)

# Action 2: คำนวณมูลค่าคลังสินค้าทั้งหมด
total_value = calculate_total_value(inventory)
print(f"Total inventory value: ${total_value:.2f}")

# Action 3: หาสินค้าที่แพงที่สุด
most_expensive = find_most_expensive(inventory)
print(f"Most expensive item: {most_expensive}")

# Action 4: เพิ่ม Eggs (30 ชิ้น, $0.25) แล้วอัปเดตเป็น (50 ชิ้น, $0.30)
add_item(inventory, "Eggs", 30, 0.25)
add_item(inventory, "Eggs", 50, 0.30)

# แสดงผลคลังสินค้าล่าสุดเพื่อตรวจสอบ
print("\nUpdated Inventory:")
for item in inventory:
    print(item)