secret_number = 34
user_number = int(input("What's the secret number ? "))
           
while user_number != secret_number:
    user_number = int(input("What's the secret number ? "))
    if user_number == secret_number:
        print("GG, the secret number was 34 ! Do you know why?")
        break
    else:
        continue
