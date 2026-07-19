print("======Python Quick ======")


while True:
    print("1. Start Quiz\n2. Exit")
    try:
        user_choice=int(input("Please enter your choice 1-2: "))
    except ValueError:
        print("Invalid Input! Please enter a valid integer:")
        continue
    
    if user_choice==1:
        print("Quiz will start soon...")
        
    elif user_choice==2:
        print("Thanks for using the Quiz, Goodbye! ")
        break
    else:
        print("Invalid Input! Please enter your choice from 1 & 2:")