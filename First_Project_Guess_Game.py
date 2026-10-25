while True:
    secret_number = 7
    print("Guess the number!")
    guess = int(input())
    if guess == secret_number:
        print("You win!")
    elif guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    if guess == True:
        break
