attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],   # Day 1
    ["Alice", "Charlie", "David"],          # Day 2
    ["Alice", "Bob", "David"],              # Day 3
    ["Alice", "David", "Eve"],              # Day 4
    ["Bob", "Charlie", "David"]             # Day 5
]

days = [set(day) for day in attendance_week]

present_every_day = set.intersection(*days)


all_studdent = set.union(*days)
apsent_least_one_day = all_studdent - present_every_day


first_day_apsent_least_day = days[0] - days[1]


attdance_count = {}
for day in days:
    for student in day:
        attdance_count[student] = attdance_count.get(student, 0) + 1
uniqe_student = {
    student
    for student, count in attdance_count.items()
    if count == 1
}
print("Student who came every day", present_every_day)
print("Apsent one day",apsent_least_one_day)
print("Come on first day but apsent last day", first_day_apsent_least_day)
print("Coming for just one day", uniqe_student)
