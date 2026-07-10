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
   