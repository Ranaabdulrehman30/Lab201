
def ispalidrome(word):
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return ispalidrome(word[1:1])
        else:
            return False

def finput(filename):
    palidrome = False
    for line in open(filename, 'r'):
        if ispalidrome(line.strip()):
            palidrome = True
            print(line.strip(), "Is palidrome")
        else:
            print(line.strip(), "Not a Palidrome")
    return "Palidrome found in {}".format(filename) is palidrome




finput("input3.txt")