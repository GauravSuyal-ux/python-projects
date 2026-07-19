print("======Python Quiz ======")
questions = [
    ["Which state is known as Devbhoomi?","uttarakhand"],
    ["Which city is known as Pink City?","jaipur"],
    ["Which hill station is famous for Naini Lake?","nainital"],
]


def start_quiz():
    marks=0
    for question in questions:
        print(question[0])
        user_ans = input("Enter your answer: ").lower().strip()

        if user_ans == question[1]:
            print("Correct!")
            marks += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question[1]}")
    return marks

def show_score(marks):
    print(f"Your final score is:{marks}")



while True:
    print("1. Start Quiz\n2. Exit")
    try:
        user_choice=int(input("Please enter your choice 1-2: "))
    except ValueError:
        print("Invalid Input! Please enter a valid integer:")
        continue
    
    if user_choice==1:
        print("Quiz will start soon...")
        marks = start_quiz()
        show_score(marks)
        
    elif user_choice==2:
        print("Thanks for using the Quiz, Goodbye! ")
        break
    else:
        print("Invalid Input! Please enter your choice from 1 & 2:")