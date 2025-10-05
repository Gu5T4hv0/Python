# Ask the user for a password until they enter the correct password.
password = "coolpy123"
attempt = 0
while attempt != password:
    attempt = input("Type the right password: ")
    if attempt == password:
        print("You can pass")