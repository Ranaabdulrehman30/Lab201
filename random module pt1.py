import random
import random as r
import string

print("Random color hex: ", "#{:06x}".format(random.randint(0, 0xFFFFFF)))

max_lenght = 255
s = ""
for i in range(random.randint(1, max_lenght)):
    s += random.choice(string.ascii_letters)
print("Random Alphabetical string:", s)

print("Random number from 0 to 7 is: ", random.randint(0, 7))

print("Random multiple of 7 from 0 to 70 is : ", random.randint(0, 10)*7)