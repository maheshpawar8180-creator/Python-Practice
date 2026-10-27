from getpass import getpass

# Practice-only example credentials. Do not use real passwords in source code.
EXPECTED_NAME = "Demo Student"
EXPECTED_EMAIL = "student@example.com"
EXPECTED_PASSWORD = "practice123"

user_name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
password = getpass("Enter your password: ")

if (
    user_name == EXPECTED_NAME
    and email == EXPECTED_EMAIL
    and password == EXPECTED_PASSWORD
):
    print(f"Welcome, {user_name}!")
else:
    print("The name, email, or password is incorrect.")
