

LIST = []

size = int(input("Enter the size of the list."))

for x in range(size):
    value = int(input("Enter the value you want to insert in the list."))
    LIST.append(value)

print(LIST)

print("NESTED LISTTTTT")

LIST_A = []

size = int(input("Enter the size of nested list. "))

for y in range(size):
    print("Enter elements of nest list {}")
    ele = [input(), input(), input(), input()]
    LIST_A.append(ele)

print(LIST_A)


LIST_B = [2, 2, 2, 2, 2]

print("CHECK SAME LIST CODE.")

fst = LIST_B[1]

dec = True

for x in LIST_B:
    if LIST_B[x] != fst:
        dec = False
        break
if dec:
    print("Same")

else:
    print("Not same")

