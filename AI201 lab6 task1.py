
def end_corona(a, b, c):
    count = 0
    while c >= 0:
        c = (c-a) + b
        count = count+1
    return count


print(end_corona(4000, 2000, 77000))
print(end_corona(3000, 2000, 50699))
print(end_corona(30000, 25000, 390205))