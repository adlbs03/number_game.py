
while True:
    user_password = input("Enter a password: ")

    if len(user_password) < 6 or user_password.isdigit():
        user_password
    else:
        print("Your password is good")
        break