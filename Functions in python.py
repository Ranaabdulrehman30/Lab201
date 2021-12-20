
#Q1. function to find max of three numbers.
def max_two(x, y):
    if x > y:
        return x
    else:
        return y

def max_three(x, y, z):
    return max_two(z, max_two(x, y))


result = max_three(5, 6, 2)

print("Max of the three number is : ", result)

LIST = []   # empty list
size = int(input("Enter the size of the list :"))

for x in range(0, size):
    value = int(input("Enter thr value in the list : "))
    LIST.append(value)

print(LIST)

def sum_of_list():
    Sum = sum(LIST)

    return Sum
print("The sum of the list is : ", sum_of_list())

def multiply_list():
    multiply = 1
    for y in range(0, size):
        multiply = multiply*LIST[y]

    return multiply

print("The multiple of the list iis : ", multiply_list())


def str_reverse(line):
    str1 = ''
    index = len(line)
    while index > 0:
        str1 += line[index - 1]
        index = index - 1
    return str1

print(str_reverse("Hello jee"))



print("The reverse order of the string is : ", str_reverse("Hello Jee"))
