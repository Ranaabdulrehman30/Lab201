

with open("input2.txt", 'r') as f:
    l1 = list(f.readline())
    l2 = list(f.readline())
    l3 = list(f.readline())
    l4 = list(f.readline())
count = 0

if l1[0] == '1':
    if l1[1] == '1':
        count += 1

for x in range(0, len(l1)):
    if l1[x] == '0' and l1[x+1] == '1':
        if l1[x+2] == '1':
            count += 1

print(count)

count1 = 0

if l2[0] == '1':
    if l2[1] == '1':
        count1 += 1

for x in range(0, len(l2)):
    if l2[x] == '0' and l2[x+1] == '1':
        if l2[x+2] == '1':
            count1 += 1

print(count1)


count2 = 0

if l3[0] == '1':
    if l3[1] == '1':
        count2 += 1

if l3[len(l3)-1] == '1':
    if l3[len(l3)-2] == '1':
        count2 += 1


for x in range(0, len(l3)):
    if l3[x] == '0' and l3[x+1] == '1':
        if l3[x+2] == '1':
            count2 += 1

print(count2)

LIST = [count, count1, count2]

print(LIST)
