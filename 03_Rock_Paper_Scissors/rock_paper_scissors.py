import random 


print("====== Rock Paper Scissors ======")

def get_computer_choice():
    choices=["rock","paper","scissors"]
    return(random.choice(choices))

def get_user_choice():
    while True:
        user_choice=input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ["rock","paper","scissors"]:
            return user_choice    
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    
    elif(
        (user_choice=="rock" and computer_choice=="scissors")
        or 
        (user_choice=="scissors" and computer_choice=="paper" )
        or
        (user_choice=="paper" and computer_choice=="rock")
    ):
        return "You Win"

    else:
        return"Computer Wins"

def play_game():
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    result= decide_winner(user_choice, computer_choice)
    print(f"You chose:{user_choice}")
    print(f"Computer chose:{computer_choice}")
    print(result) 
      
while True:
    play_game()
    choice=input("Play Again?(y/n)").lower().strip()
    if choice == "n":
        print("Thank You for playing... ")
        break
    elif choice == "y":
        continue
    else:
        print("Invalid Choice! Please choose (y or n)")


