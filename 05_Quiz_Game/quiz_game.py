import random
print("======Python Quiz ======")
questions = [
    ["Which state is known as Devbhoomi?","uttarakhand"],
    ["Which city is known as Pink City?","jaipur"],
    ["Which hill station is famous for Naini Lake?","nainital"],
]


def start_quiz():
    marks=0
    for question_no,question in enumerate(questions,start=1):
        print(f"\nQuestion {question_no}:")
        print(question[0])
        user_ans = input("Enter your answer: ").lower().strip()

        if user_ans == question[1]:
            print("Correct!")
            marks += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question[1]}")
    return marks


def show_score(marks,total_questions) :
    print(f"Your final score is: {marks}/{total_questions}\n")



while True:
    print("1. Start Quiz\n2. Exit")
    try:
        user_choice=int(input("Please enter your choice 1-2: "))
    except ValueError:
        print("Invalid Input! Please enter a valid integer:")
        continue

    if user_choice==1:
        print("\nQuiz will start soon...\n")
        play_again= True

        while play_again:
            random.shuffle(questions)
            marks = start_quiz()
            show_score(marks,len(questions))
            
            while True:
                replay_input=input("Do you want to play again? '(y/n)':").lower().strip()                
                if replay_input=="y":
                    print("Quiz Starting again...")
                    break
                elif replay_input=="n":
                    play_again=False
                    print("Thank you for playing.")
                    break
                else:
                    print("Invalid input! Please enter 'y' or 'n'.")
                    

    elif user_choice==2:
        print("Thanks for using the Quiz, Goodbye! ")
        break
    else:
        print("Invalid Input! Please enter your choice from 1 & 2:")