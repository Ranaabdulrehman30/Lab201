def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


# check the above function

ENCRYPTEDTEST = str(input("Enter your text :"))

s = int(input("Enter your shift"))

print("Original Text: ", ENCRYPTEDTEST)
print("Shift key: ", s)
print("Encrypted String:", encrypt(ENCRYPTEDTEST, s))

# check the above function
ENCRYPTEDTEST = str(input("Enter your text :"))

s = int(input("Enter your shift"))

print("Encrypted Text: ", ENCRYPTEDTEST)
print("Shift key: ", s)
print("Original String:", decrypt(ENCRYPTEDTEST, s))
