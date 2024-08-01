ch=input("Enter a Character")
if ch<='9' and ch>='0':
    print("Character is a Digit")

if ch.isupper():
    print("Uppercase")

if ch.islower():
    print("Lowercase")

else:
    print("Special Character")