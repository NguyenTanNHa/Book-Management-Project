toal1 = 0
toal2 = 0

day1 = int(input("employee 1: how many days? "))
for i in range(1, day1 + 1):
    hours = int(input("hours? "))
    if hours <= 8:
        toal1 = toal1 + hours
    else:
        toal1 = toal1 + 8

print("Employee 1's total hours = " + str(toal1) + " (" + str(toal1 // 3) + " day)")

day2 = int(input("employee 2: how many days? "))
for i in range(1, day2 + 1):
    hours = int(input("hours? "))
    if hours <= 8:
        toal2 = toal2 + hours
    else:
        toal2 = toal2 + 8

print("Employee 2's total hours = " + str(toal2) + " (" + str(toal2 // 2) + " day)")
print("Total hours for both: ", toal1 + toal2)
