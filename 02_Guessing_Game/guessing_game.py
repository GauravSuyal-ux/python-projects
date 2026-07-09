import random
while True:
    secret_num = random.randint(1, 100)
    count = 1

    print("====== Guess the Number Between 1-100 ======")

    while True:
        try:
            guess = int(input("Guess the number: "))

        except ValueError:
            print("Invalid input! Enter an integer between 1 and 100.")
            continue

        if 1 <= guess <= 100:

            if guess == secret_num:
                print(f"Yes! That's correct. The number is {secret_num}.")
                print(f"You guessed it in {count} attempts.")
                break

            elif guess > secret_num:
                print("You guessed a greater number. Try a smaller one.")
                count += 1

            else:
                print("You guessed a smaller number. Try a greater one.")
                count += 1

        else:
            print("Please enter a number between 1 and 100.")
            continue
    
    while True:
        choice= input("Play again?? (y/n)").lower()

        if choice == "y":
            break
        elif choice=="n":
            print("Thanks for playing!...") 
            exit()
        else:
            print("Please enter a valid choice 'y' or 'n':")
