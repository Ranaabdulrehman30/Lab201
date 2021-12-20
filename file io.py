try:
    with open("txt.txt", 'r') as f:
        lines = f.read()
        for x in lines:
            line = lines.split("\n")
        print(line)
except FileNotFoundError:
    print("File not found, Dear")

