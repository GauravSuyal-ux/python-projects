import random 
print("====== Rock Paper Scissors ======")

def get_computer_choice():
    choices=["rock","paper","scissors"]
    return(random.choice(choices))
    
get_computer_choice()
   