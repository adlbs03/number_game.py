secret_number = 1
user_number = int(input("What's the secret number ? "))

def indice():
    print("There is a link with Stranger Things")
    return
           
while user_number != secret_number:
    user_number = int(input("What's the secret number ? "))
    if user_number == secret_number:
        print("GG, the secret number was 34 ! Do you know why?")
        break
    else:
        indice()
        continue
