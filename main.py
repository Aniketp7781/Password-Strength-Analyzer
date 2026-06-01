from password_checker import check_password_strength
from password_generator import generate_password
from hashing import hash_password

print("=== Password Strength Analyzer ===")

password = input("Enter your password: ")

# check strength
result = check_password_strength(password)
print("Password Strength:", result)

# suggestion (for weak + medium)
if result != "Strong Password":
    print("Suggested Strong Password:", generate_password())

# hashing
hashed = hash_password(password)
print("Encrypted Password:", hashed)