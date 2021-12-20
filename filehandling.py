import pickle

f = open("filee.txt", "r")
lines = f.readline()
print(lines)
count = 0
for line in f:
    if line[0] != "T":
        count +=1
f.close()

print("Number of line starting with T are : " + str(count))

DIC = {1: "hello", 2: "Hi", 3: "BYE"}

f2 = open("Hi.txt", "wb")
pickle.dump(DIC, f2)

f2.close()

f2 = open("Hi.txt", "rb")
output = pickle.load(f2)

print(output)

details = {'Name': "Alice",
           'Age': 21,
           'Degree': "Bachelor Cse",
           'University': "Northeastern Univ"}

with open("myfile.txt", 'w') as f:
    for key, value in details.items():
        f.write('%s:%s\n' % (key, value))




