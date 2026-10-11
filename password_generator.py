
import string
import secrets

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Please enter a length of at least 4.")
else:
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("Generated Password:", password)
