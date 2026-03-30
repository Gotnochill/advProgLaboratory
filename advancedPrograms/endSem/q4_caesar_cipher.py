text = "HelloWorld"
key = 3
encrypted = ""

for char in text:
    shift = 65 if char.isupper() else 97
    encrypted += chr((ord(char) - shift + key) % 26 + shift)

print("Encrypted:", encrypted)
