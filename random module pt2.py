import os
import random

LIST = [1, 2, 4, 45, 664, 75, 75, 90, 23]
SET = set(LIST)
DICT = {"a": 1, "b": 34, "c": 45, "d": 78}

print("Random Element from list: ", random.choice(LIST))
print("Random Element fromm the SET: ", random.choice(tuple(SET)))
d = random.choice(list(DICT))
print("Random Element from the Dictionary: ", DICT[d])

print("Print a random file from a Directory: ", random.choice(os.listdir("/")))