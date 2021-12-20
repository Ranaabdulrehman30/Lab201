
def sameElement(set_a, set_b):
    set_c = (set_a.union(set_b)-(set_a.intersection(set_b)))

    return set_c


print("The elements in A or B but not both are : " + str(sameElement({1, 2, 3, 4, 3, 5, 7}, {1, 9, 10, 5, 7, 3, 11, 12})))