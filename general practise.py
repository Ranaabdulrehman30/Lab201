
print("I am best in the World, no body can touch me.")

MYLIST = ['me', 'you', 'us']

print(MYLIST)

print(dir(MYLIST))

MYLIST.__delitem__(1)

print(MYLIST)

print(help(MYLIST.__hash__))


pair = (3, 4)

print(pair)

x, y = pair  # NUMBER OF VARIABLES AND SIZE OF THE TUPLE SHOULD BE SAME

print(x)

shapes = ['Circle', 'Triangle', 'Rectangle', 'Square', 'Circle']

print(shapes)

set_of_shapes = set(shapes)

print(set_of_shapes)

print('Circle' in set_of_shapes)

# Implementing Dictionary

DICK = {'rana': "sexy", 'faizan': " EWWWWWW", 'areeba': " LOVE"}

print(DICK)

DICK['rana'] = {"sexy", "Chicken piece"}

print(DICK)

l1 = [1, 2, 3, 4, 5]
l2 = ['A', 'B', 'C', 'D', 'F']

D = dict(zip(l1, l2))

print(D)
